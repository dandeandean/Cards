package cards

import (
	"encoding/csv"
	"fmt"
	"os"

	"github.com/dandeandean/cards/core"
	"github.com/spf13/cobra"
)

func CardsFromCsv(fName string) []core.Card {
	if len(fName) > 4 && fName[len(fName)-4:] != ".csv" {
		fName += ".csv"
	}
	f, err := os.Open(fName)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	lines, err := csv.NewReader(f).ReadAll()
	if err != nil {
		panic(err)
	}
	cards := make([]core.Card, 0)
	for _, line := range lines {
		if len(line) >= 2 {
			cards = append(cards, core.Card{
				Front: line[0],
				Back:  line[1],
			})
		}
	}
	return cards
}

var showCmd = &cobra.Command{
	Use:   "show",
	Short: "Show Cards in File",
	Long:  "Show Cards in File.",
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) != 1 {
			fmt.Println("Usage: cards practice <dir>")
			return
		}
		dir := args[0]
		cards := CardsFromCsv(dir)
		for _, c := range cards {
			fmt.Println(c.String())
		}
	},
}

var makeCmd = &cobra.Command{
	Use:   "make",
	Short: "todo",
	Long:  "todo",
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) != 3 {
			fmt.Println("Usage: cards practice <dir> <front> <back>")
			return
		}
		dir, front, back := args[0], args[1], args[2]
		c := core.Card{Front: front, Back: back}
		fmt.Println(c.String(), dir)
		err := c.DumpToCsv(dir)
		if err != nil {
			panic(err)
		}
	},
}

func init() {
	rootCmd.AddCommand(showCmd)
	rootCmd.AddCommand(makeCmd)
}
