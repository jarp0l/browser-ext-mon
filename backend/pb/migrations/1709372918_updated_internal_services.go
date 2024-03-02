package migrations

import (
	"encoding/json"

	"github.com/pocketbase/dbx"
	"github.com/pocketbase/pocketbase/daos"
	m "github.com/pocketbase/pocketbase/migrations"
	"github.com/pocketbase/pocketbase/models/schema"
)

func init() {
	m.Register(func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("1smri0lhc3uo18h")
		if err != nil {
			return err
		}

		// update
		edit_service_name := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "mwsgcgdn",
			"name": "service_name",
			"type": "text",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), edit_service_name)
		collection.Schema.AddField(edit_service_name)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("1smri0lhc3uo18h")
		if err != nil {
			return err
		}

		// update
		edit_service_name := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "mwsgcgdn",
			"name": "service_name",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), edit_service_name)
		collection.Schema.AddField(edit_service_name)

		return dao.SaveCollection(collection)
	})
}
