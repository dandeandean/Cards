package util

import (
	"encoding/csv"
	"github.com/dandeandean/cards/core"
	"os"
)

func CardsFromCsv(fName string) []core.Card {
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
