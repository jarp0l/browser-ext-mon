/*
Copyright © 2024 Prajwol Pradhan <57973356+jarp0l@users.noreply.github.com>
*/
package cmd

import (
	"context"
	"fmt"
	"os"
	"os/signal"
	"sync"
	"syscall"
	"time"

	"github.com/spf13/cobra"
)

// headlessCmd represents the headless command
var headlessCmd = &cobra.Command{
	Use:   "headless",
	Short: "Run bem-cli in headless mode",
	Long:  ``,
	Run: func(cmd *cobra.Command, args []string) {
		// Create a context that can be canceled
		ctx, cancel := context.WithCancel(context.Background())

		// Use a WaitGroup to wait for goroutines to finish
		var wg sync.WaitGroup

		// Start the background monitoring goroutine
		wg.Add(1)
		go monitorActivities(ctx, &wg)

		// Set up a signal handler to gracefully terminate the program
		signalCh := make(chan os.Signal, 1)
		signal.Notify(signalCh, os.Interrupt, syscall.SIGTERM)

		// Wait for a termination signal
		sig := <-signalCh
		fmt.Printf("Received signal: %v\n", sig)
		cancel() // Signal to stop background goroutines

		// Wait for all goroutines to finish
		wg.Wait()

		fmt.Println("Main program terminated.")
	},
}

func init() {
	rootCmd.AddCommand(headlessCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// headlessCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// headlessCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}

func monitorActivities(ctx context.Context, wg *sync.WaitGroup) {
	defer wg.Done()

	for {
		select {
		case <-ctx.Done():
			fmt.Println("Monitoring stopped.")
			return
		default:
			// Your monitoring logic goes here
			fmt.Println("Monitoring activities...")
			time.Sleep(2 * time.Second)
		}
	}
}
