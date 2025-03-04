package cards

import (
	"fmt"

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
	},
}

func init() {
	rootCmd.AddCommand(practiceCmd)
}
