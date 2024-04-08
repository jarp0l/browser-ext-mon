/*
Copyright © 2024 Prajwol Pradhan <57973356+jarp0l@users.noreply.github.com>
*/
package cmd

import (
	"os"
	"os/exec"
	"path"

	"github.com/charmbracelet/log"
	"github.com/spf13/cobra"
	"github.com/spf13/viper"
)

// startCmd represents the start command
var startCmd = &cobra.Command{
	Use:   "start",
	Short: "Start monitoring extensions",
	Run: func(cmd *cobra.Command, args []string) {
		startMonitoring()
	},
}

func init() {
	rootCmd.AddCommand(startCmd)
}

func startMonitoring() {
	_, err := exec.LookPath("osqueryd")
	if err != nil {
		log.Fatal("osquery not found in PATH. Please install osquery first.")
	}

	if err := viper.GetViper().ReadInConfig(); err != nil {
		log.Fatal(err.Error())
	}

	// This may need to be implemented later for pid, for now --ephemeral is used.
	// --pidfile=$(echo $$)

	cmd := exec.Command("osqueryd",
		"--host_identifier=uuid",
		"--tls_hostname=localhost",
		"--tls_server_certs="+path.Join("osquery", "root.crt"),
		"--enroll_secret_path="+viper.GetViper().ConfigFileUsed(),
		"--config_plugin=tls",
		"--logger_plugin=tls",
		"--enroll_tls_endpoint=/osquery/enroll",
		"--logger_tls_endpoint=/osquery/logger",
		"--config_tls_endpoint=/osquery/config",
		"--ephemeral",
		"--disable_database")

	// Connect stdout and stderr of osqueryd to the cli
	// https://blog.kowalczyk.info/article/wOYk/advanced-command-execution-in-go-with-osexec.html
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	err = cmd.Run()
	if err != nil {
		log.Fatal(err.Error())
	}
}
