/*
Copyright © 2024 Prajwol Pradhan <57973356+jarp0l@users.noreply.github.com>
*/
package cmd

import (
	"os"
	"os/exec"

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

var rootcrt = `	
-----BEGIN CERTIFICATE-----
MIIBozCCAUqgAwIBAgIRAKXr3CWNTExltqAh+tqthU4wCgYIKoZIzj0EAwIwMDEu
MCwGA1UEAxMlQ2FkZHkgTG9jYWwgQXV0aG9yaXR5IC0gMjAyNCBFQ0MgUm9vdDAe
Fw0yNDAyMjQxMDI5MDFaFw0zNDAxMDIxMDI5MDFaMDAxLjAsBgNVBAMTJUNhZGR5
IExvY2FsIEF1dGhvcml0eSAtIDIwMjQgRUNDIFJvb3QwWTATBgcqhkjOPQIBBggq
hkjOPQMBBwNCAASYC6AZUWu3cFiYJ1tZ6X1sLZZUXTulgGsUXAUEtPom4/i0idyp
t9sqRkV0JqwTnRHutCs0pTUPkVpQEpIzhrZDo0UwQzAOBgNVHQ8BAf8EBAMCAQYw
EgYDVR0TAQH/BAgwBgEB/wIBATAdBgNVHQ4EFgQUcoGjN3nb7JDZzgylgMwBOS6i
lVgwCgYIKoZIzj0EAwIDRwAwRAIgbdN9S0+x/UbuE8tvFmENg/UcwDS2RRF3PKXB
W+1HcrUCIC95H+N1SPmXSQASQyLLzhs7HT3lzYiHaF82sj3yCPQc
-----END CERTIFICATE-----
`

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

	// Create temporary file
	// We need to create a temporary file to store the root cert;
	// it avoids the need to ship a separate root cert file with the cli binary.
	tempFile, err := os.CreateTemp(os.TempDir(), "bem-cli-root.crt")
	if err != nil {
		log.Fatal("Error creating temporary file:", err)
	}
	defer os.Remove(tempFile.Name())

	// Write the string to the temporary file
	_, err = tempFile.WriteString(rootcrt)
	if err != nil {
		log.Fatal("Error writing to temporary file:", err)
	}

	// This may need to be implemented later for pid, for now --ephemeral is used.
	// --pidfile=$(echo $$)

	cmd := exec.Command("osqueryd",
		"--host_identifier=uuid",
		"--tls_hostname=localhost",
		"--tls_server_certs="+tempFile.Name(),
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
