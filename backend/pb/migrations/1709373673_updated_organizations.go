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

		// add
		new_api_key := &schema.SchemaField{}
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
		}`), new_api_key)
		collection.Schema.AddField(new_api_key)

		// update
		edit_admin_id := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "75ahp2qq",
			"name": "admin_id",
			"type": "relation",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"collectionId": "_pb_users_auth_",
				"cascadeDelete": true,
				"minSelect": null,
				"maxSelect": 1,
				"displayFields": null
			}
		}`), edit_admin_id)
		collection.Schema.AddField(edit_admin_id)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("bxllu29bavy3izv")
		if err != nil {
			return err
		}

		// remove
		collection.Schema.RemoveField("qxgdgzgr")

		// update
		edit_admin_id := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "75ahp2qq",
			"name": "admin_id",
			"type": "relation",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"collectionId": "_pb_users_auth_",
				"cascadeDelete": true,
				"minSelect": null,
				"maxSelect": 1,
				"displayFields": null
			}
		}`), edit_admin_id)
		collection.Schema.AddField(edit_admin_id)

		return dao.SaveCollection(collection)
	})
}
