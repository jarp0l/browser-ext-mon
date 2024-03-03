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
		edit_service_token := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "vgusewui",
			"name": "service_token",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), edit_service_token)
		collection.Schema.AddField(edit_service_token)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("1smri0lhc3uo18h")
		if err != nil {
			return err
		}

		// update
		edit_service_token := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "vgusewui",
			"name": "api_token",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), edit_service_token)
		collection.Schema.AddField(edit_service_token)

		return dao.SaveCollection(collection)
	})
}
