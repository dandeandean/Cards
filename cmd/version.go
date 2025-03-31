package cards

import (
	"fmt"
	"github.com/spf13/cobra"
)

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "Print the version number of Cards",
	Long:  `All software has versions. This is Cards'`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Cards CLI v0.0.0 prerelease alpha beta")
	},
}

func init() {
	rootCmd.AddCommand(versionCmd)
}
