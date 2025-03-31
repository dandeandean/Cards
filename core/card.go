package core

import (
	"encoding/csv"
	"os"
)

type Card struct {
	Front string
	Back  string
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
	err = w.Write([]string{c.Front, c.Back})
	defer w.Flush()
	if err != nil {
		panic(err)
	}
	return err
}

func (c Card) String() string {
	return c.Front + " | " + c.Back
}
