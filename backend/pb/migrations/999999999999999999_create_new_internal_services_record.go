package migrations

import (
	"github.com/google/martian/v3/log"
	"github.com/pocketbase/dbx"
	"github.com/pocketbase/pocketbase/daos"
	m "github.com/pocketbase/pocketbase/migrations"
	"github.com/pocketbase/pocketbase/models"
)

func init() {
	m.Register(func(db dbx.Builder) error {
		dao := daos.New(db)

		collection, err := dao.FindCollectionByNameOrId("internal_services")
		if err != nil {
			return err
		}

		record := models.NewRecord(collection)
		record.Set("service_name", "osquery-be")
		record.Set("service_token", "osquery-be")

		return dao.SaveRecord(record)
	}, func(db dbx.Builder) error {
		log.Errorf("down migration not implemented")
		return nil
	})
}
