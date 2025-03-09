package cards

import (
	"encoding/csv"
	"fmt"
	"os"

	"github.com/spf13/cobra"
)

type Card struct {
	front string
	back  string
}

func (c Card) DumpToCsv(fName string) error {
	if len(fName) > 4 && fName[len(fName)-4:] != ".csv" {
		fName += ".csv"
	}
	f, err := os.OpenFile(fName, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		panic(err)
	}
	defer f.Close()
	w := csv.NewWriter(f)
	err = w.Write([]string{c.front, c.back})
	defer w.Flush()
	if err != nil {
		panic(err)
	}
	return err
}

func CardsFromCsv(fName string) []Card {
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
	cards := make([]Card, 0)
	for _, line := range lines {
		if len(line) >= 2 {
			cards = append(cards, Card{line[0], line[1]})
		}
	}
	return cards
}

func (c Card) String() string {
	return c.front + " | " + c.back
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
		c := Card{front: front, back: back}
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
