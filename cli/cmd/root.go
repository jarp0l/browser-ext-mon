/*
Copyright © 2024 Prajwol Pradhan <57973356+jarp0l@users.noreply.github.com>
*/
package cmd

import (
	// "fmt"
	"os"
	"path"
	// "strings"

	"github.com/charmbracelet/log"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

var cfgFile string
var debug bool

// var overwriteFile string = "n"

// rootCmd represents the base command when called without any subcommands
var rootCmd = &cobra.Command{
	Use:   "bem-cli",
	Short: "CLI tool for browser-ext-mon project",
	Long: `This tool is used to send information about installed extensions from
nodes to backend server.`,
	PersistentPreRun: func(cmd *cobra.Command, args []string) {
		if debug {
			log.SetLevel(log.DebugLevel)
		}
	},
	// Uncomment the following line if your bare application
	// has an action associated with it:
	// Run: func(cmd *cobra.Command, args []string) { },
}

// Execute adds all child commands to the root command and sets flags appropriately.
// This is called by main.main(). It only needs to happen once to the rootCmd.
func Execute() {
	err := rootCmd.Execute()
	if err != nil {
		os.Exit(1)
	}
}

func init() {
	cobra.OnInitialize(initConfig)

	// Here you will define your flags and configuration settings.
	// Cobra supports persistent flags, which, if defined here,
	// will be global for your application.

	rootCmd.PersistentFlags().StringVarP(&cfgFile, "config", "c", "", "path to config file (default is $HOME/bem.json)")
	rootCmd.PersistentFlags().BoolVarP(&debug, "debug", "d", false, "enable verbose logging")

	// Cobra also supports local flags, which will only run
	// when this action is called directly.
	// rootCmd.Flags().BoolP("toggle", "t", false, "help message for toggle")
}

// initConfig reads in config file and ENV variables if set.
func initConfig() {
	if cfgFile != "" {
		// Use config file from the flag.
		viper.SetConfigFile(cfgFile)
	} else {
		// Find user home directory.
		home, err := os.UserHomeDir()
		cobra.CheckErr(err)
		viper.SetConfigFile(path.Join(home, "bem.json"))
	}

	viper.AutomaticEnv() // read in environment variables that match

	if err := viper.ReadInConfig(); err != nil {
		log.Error(err)

		log.Info("Config file not found. Creating a new one...")
		// Write the default config file if it doesn't exist
		if err := viper.WriteConfigAs(viper.ConfigFileUsed()); err != nil {
			log.Error(err)
		}
	}

	// Consider this method for future refactoring: https://github.com/spf13/viper/issues/1#issuecomment-451533395
	// if _, err := os.Stat(viper.ConfigFileUsed()); err == nil {
	// 	fmt.Print("Config file already exists. Do you want to overwrite it? (y/N): ")
	// 	fmt.Scanf("%s", &overwriteFile)

	// 	if strings.ToLower(overwriteFile) != "y" {
	// 		log.Info("Not overwriting config file. Exiting...")
	// 		os.Exit(1)
	// 	}
	// }
	log.Debugf("Using config file: %s", viper.ConfigFileUsed())
}
