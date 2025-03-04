package cards

import (
	"fmt"
	"github.com/spf13/cobra"
	"os"
)

var rootCmd = &cobra.Command{
	Use:   "cards",
	Short: "Cards is a cli flashcard gadget.",
	Long:  "Cards is a cli flashcard gadget.",
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Flashcards")
	},
}

func Execute() {
	if err := rootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(1)
	}
}
