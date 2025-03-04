package cards

import (
	"encoding/csv"
	"os"
)

type Card struct {
	front string
	back  string
}

func CardsFromCsv(fName string) []Card {
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
