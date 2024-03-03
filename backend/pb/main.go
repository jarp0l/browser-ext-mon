package main

import (
	"log"
	"net/http"
	"os"
	"strings"

	_ "github.com/jarp0l/browser-ext-mon/backend/pb/migrations"
	"github.com/labstack/echo/v5"
	"github.com/pocketbase/pocketbase"
	"github.com/pocketbase/pocketbase/apis"
	"github.com/pocketbase/pocketbase/core"
	"github.com/pocketbase/pocketbase/models"
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

	// serves static files from the provided public dir (if exists)
	app.OnBeforeServe().Add(func(e *core.ServeEvent) error {
		e.Router.GET("/healthz", func(c echo.Context) error {
			return c.String(http.StatusOK, "OK")
		}, apis.ActivityLogger(app))
		e.Router.GET("/*", apis.StaticDirectoryHandler(os.DirFS("./pb_public"), false))
		return nil
	})

	// only fire when a record on "users" collection is created
	app.OnRecordBeforeCreateRequest("users").Add(func(e *core.RecordCreateEvent) error {
		organizations_collection, err := app.Dao().FindCollectionByNameOrId("organizations")
		if err != nil {
			return err
		}

		organizations_record := models.NewRecord(organizations_collection)
		organizations_record.Set("name", e.Record.Get("org_name"))
		// admin_email is redundant, but it's used to find the organization record after the user is created
		// we can't set admin_id yet as the user record is not created yet
		organizations_record.Set("admin_email", e.Record.Get("email"))

		if err := app.Dao().SaveRecord(organizations_record); err != nil {
			return err
		}

		return nil
	})

	// only fire when a record on "users" collection is created
	app.OnRecordAfterCreateRequest("users").Add(func(e *core.RecordCreateEvent) error {
		organizations_record, err := app.Dao().FindFirstRecordByData("organizations", "admin_email", e.Record.Get("email"))
		if err != nil {
			return err
		}

		organizations_record.Set("admin_id", e.Record.Get("id"))
		apiKey := security.RandomString(16)
		organizations_record.Set("api_key", apiKey)

		if err := app.Dao().SaveRecord(organizations_record); err != nil {
			return err
		}
		return nil
	})

	if err := app.Start(); err != nil {
		log.Fatal(err)
	}
}
