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

		collection, err := dao.FindCollectionByNameOrId("bxllu29bavy3izv")
		if err != nil {
			return err
		}

		// update
		edit_api_key := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "qxgdgzgr",
			"name": "api_key",
			"type": "text",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"min": 10,
				"max": 15,
				"pattern": ""
			}
		}`), edit_api_key)
		collection.Schema.AddField(edit_api_key)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("bxllu29bavy3izv")
		if err != nil {
			return err
		}

		// update
		edit_api_key := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "qxgdgzgr",
			"name": "api_key",
			"type": "text",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), edit_api_key)
		collection.Schema.AddField(edit_api_key)

		return dao.SaveCollection(collection)
	})
}
