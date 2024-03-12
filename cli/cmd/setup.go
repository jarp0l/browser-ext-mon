/*
Copyright © 2024 Prajwol Pradhan <57973356+jarp0l@users.noreply.github.com>
*/
package cmd

import (
	"fmt"

	"github.com/charmbracelet/log"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var apiKey string
var ownerEmail string

// setupCmd represents the setup command
var setupCmd = &cobra.Command{
	Use:   "setup",
	Short: "Setup the bem-cli tool for first time use",
	Long:  `This command will guide you through the process of setting up the bem-cli tool for first time use.`,
	Run: func(cmd *cobra.Command, args []string) {
		setup()
	},
}

func init() {
	rootCmd.AddCommand(setupCmd)
}

func setup() {
	log.Info("Seting up bem-cli tool for first time use.")

	for {
		fmt.Print("Enter API key: ")
		fmt.Scanf("%s", &apiKey)

		if apiKey == "" {
			log.Error("API key field cannot be empty.")
			continue
		} else {
			break
		}
	}

	// Owner email (or the email of the owner of the device)
	// Optional
	fmt.Print("Enter owner email: ")
	fmt.Scanf("%s", &ownerEmail)
	if ownerEmail == "" {
		log.Warn("Owner email not set.")
	}

	viper.GetViper().Set("api_key", apiKey)
	viper.GetViper().Set("owner_email", ownerEmail)
	if err := viper.GetViper().WriteConfig(); err != nil {
		log.Error(err)
		return
	}

	log.Debugf("API key: %s", viper.GetViper().GetString("api_key"))
	log.Debugf("Owner email: %s", viper.GetViper().GetString("owner_email"))
	log.Info("API key and owner email set successfully.")
}
