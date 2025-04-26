package cards

import (
	"os"
	"strings"

	"github.com/spf13/cobra"
)

func getSetsCmp(cmd *cobra.Command, args []string, toComplete string) ([]cobra.Completion, cobra.ShellCompDirective) {
	dirBase := os.Getenv("CARDSHOME")
	if dirBase == "" {
		dirBase = "./"
	}
	files, _ := os.ReadDir(dirBase)
	fileNames := make([]string, 0)
	for _, f := range files {
		fName := f.Name()
		if strings.Contains(fName, ".csv") &&
			len(fName) > 4 &&
			fName[len(fName)-4:] == ".csv" {
			fileNames = append(fileNames, fName[0:len(fName)-4])
		}
	}
	return fileNames, cobra.ShellCompDirectiveNoFileComp
}
