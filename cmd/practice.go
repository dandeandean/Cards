package cards

import (
	"fmt"
	"os"

	tea "github.com/charmbracelet/bubbletea"
	"github.com/dandeandean/cards/core"
	"github.com/dandeandean/cards/core/util"
	"github.com/spf13/cobra"
)

var practiceCmd = &cobra.Command{
	Use:   "practice",
	Short: "Practice",
	Long:  "Practice takes one argument, the path to the csv.",
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) != 1 {
			fmt.Println("Usage: cards practice <dir>")
			return
		}
		dir := args[0]
		p := tea.NewProgram(practiceModel(dir))
		if _, err := p.Run(); err != nil {
			fmt.Printf("Alas, there's been an error: %v", err)
		}
	},
	ValidArgsFunction: getSetsCmp,
}

var NumberToPractice int

func init() {
	rootCmd.AddCommand(practiceCmd)
	practiceCmd.PersistentFlags().IntVarP(&NumberToPractice, "number", "n", 5, "number of cards to show")
}

type model struct {
	choices  []core.Card      // items on the to-do list
	cursor   int              // which to-do list item our cursor is pointing at
	selected map[int]struct{} // which to-do items are selected
}

func (m model) Init() tea.Cmd {
	// Just return `nil`, which means "no I/O right now, please."
	return nil
}

func (m model) Update(msg tea.Msg) (tea.Model, tea.Cmd) {
	switch msg := msg.(type) {

	// Is it a key press?
	case tea.KeyMsg:

		// Cool, what was the actual key pressed?
		switch msg.String() {

		// These keys should exit the program.
		case "ctrl+c", "q":
			return m, tea.Quit

		// The "up" and "k" keys move the cursor up
		case "up", "k":
			if m.cursor > 0 {
				m.cursor--
			}

		// The "down" and "j" keys move the cursor down
		case "down", "j":
			if m.cursor < len(m.choices)-1 {
				m.cursor++
			}

		// The "enter" key and the spacebar (a literal space) toggle
		// the selected state for the item that the cursor is pointing at.
		case "enter", " ":
			_, ok := m.selected[m.cursor]
			if ok {
				delete(m.selected, m.cursor)
			} else {
				m.selected[m.cursor] = struct{}{}
			}
		}
	}

	// Return the updated model to the Bubble Tea runtime for processing.
	// Note that we're not returning a command.
	return m, nil
}

func (m model) View() string {
	// The header
	s := "Think real hard about the phrase before showing it\n\n"

	// Iterate over our choices
	for i, choice := range m.choices {

		// Is the cursor pointing at this choice?
		cursor := " " // no cursor
		if m.cursor == i {
			cursor = ">" // cursor!
		}

		// Is this choice selected?
		checked := " " // not selected
		if _, ok := m.selected[i]; ok {
			checked = "x" // selected!
		}

		// Render the row
		cardRepr := choice.Front
		if checked == "x" {
			cardRepr += " | " + choice.Back
		}
		s += fmt.Sprintf("%s [%s] %s\n", cursor, checked, cardRepr)
	}

	// The footer
	s += "\nPress q to quit.\n"

	// Send the UI for rendering
	return s
}

func practiceModel(fName string) model {

	if len(fName) > 4 && fName[len(fName)-4:] != ".csv" {
		fName += ".csv"
	}
	dir := os.Getenv("CARDSHOME")
	if dir == "" {
		dir = "."
	}
	cardChoices := util.CardsFromCsv(dir + "/" + fName)
	return model{
		// Our to-do list is a grocery list
		choices: cardChoices,

		// A map which indicates which choices are selected. We're using
		// the  map like a mathematical set. The keys refer to the indexes
		// of the `choices` slice, above.
		selected: make(map[int]struct{}),
	}
}
