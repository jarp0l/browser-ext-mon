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

		collection, err := dao.FindCollectionByNameOrId("1l9pedzcwc3pf4x")
		if err != nil {
			return err
		}

		// update
		edit_org_id := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "tqygpayg",
			"name": "org_id",
			"type": "relation",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"collectionId": "bxllu29bavy3izv",
				"cascadeDelete": true,
				"minSelect": null,
				"maxSelect": 1,
				"displayFields": null
			}
		}`), edit_org_id)
		collection.Schema.AddField(edit_org_id)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("1l9pedzcwc3pf4x")
		if err != nil {
			return err
		}

		// update
		edit_org_id := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "tqygpayg",
			"name": "org_id",
			"type": "relation",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"collectionId": "bxllu29bavy3izv",
				"cascadeDelete": true,
				"minSelect": null,
				"maxSelect": 1,
				"displayFields": null
			}
		}`), edit_org_id)
		collection.Schema.AddField(edit_org_id)

		return dao.SaveCollection(collection)
	})
}
