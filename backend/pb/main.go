package main

import (
	"log"
	"net/http"
	"os"
	"strings"

	_ "github.com/jarp0l/browser-ext-mon/backend/pb/migrations"
	pb_osquery "github.com/jarp0l/browser-ext-mon/backend/pb/osquery"
	"github.com/labstack/echo/v5"
	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
	"github.com/pocketbase/pocketbase/plugins/migratecmd"
	"github.com/pocketbase/pocketbase/tools/security"
)

func main() {
	app := pocketbase.New()

	// loosely check if it was executed using "go run"
	isGoRun := strings.HasPrefix(os.Args[0], os.TempDir())

	migratecmd.MustRegister(app, app.RootCmd, migratecmd.Config{
		// enable auto creation of migration files when making collection changes in the Admin UI
		// (the isGoRun check is to enable it only during development)
		Automigrate: isGoRun,
	})

	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/healthz", func(c echo.Context) error {
			return c.String(http.StatusOK, "OK")
		}, apis.ActivityLogger(app))

		e.Router.POST("/osquery/enroll", pb_osquery.Enroll)
		e.Router.GET("/osquery/config", pb_osquery.GetConfig)
		e.Router.POST("/osquery/config", pb_osquery.PostConfig)

		// serves static files from the provided public dir (if exists)
		e.Router.GET("/*", apis.StaticDirectoryHandler(os.DirFS("./pb_public"), false))

		return nil
	})

	app.OnRecordBeforeCreateRequest().Add(func(e *core.RecordCreateEvent) error {
		if e.Record.TableName() == "organizations" {
			apiKey := security.RandomString(10)
			e.Record.Set("api_key", apiKey)
		}
		return nil
	})

	if err := app.Start(); err != nil {
		log.Fatal(err)
	}
}
