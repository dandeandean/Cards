package cards

import (
	"fmt"

	"github.com/dandeandean/cards/core"
	"github.com/dandeandean/cards/core/util"
	"github.com/spf13/cobra"
)

var showCmd = &cobra.Command{
	Use:   "show dir",
	Short: "Show Cards in File",
	Long:  "Show Cards in File.",
	Args:  cobra.MinimumNArgs(1),
	Run: func(cmd *cobra.Command, args []string) {
		if len(args) != 1 {
			fmt.Println("Usage: cards practice <dir>")
			return
		}
		dir := args[0]
		cards := util.CardsFromCsv(dir)
		for _, c := range cards {
			fmt.Println(c.String())
		}
	},
	ValidArgsFunction: getSetsCmp,
}

var makeCmd = &cobra.Command{
	Use:  "make dir front back",
	Long: "Make new card",
	Args: cobra.MinimumNArgs(3),
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
