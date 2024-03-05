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

		if err := json.Unmarshal([]byte(`[
			"CREATE UNIQUE INDEX ` + "`" + `idx_82N7Hut` + "`" + ` ON ` + "`" + `nodes` + "`" + ` (` + "`" + `uuid` + "`" + `)"
		]`), &collection.Indexes); err != nil {
			return err
		}

		// update
		edit_uuid := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
			"system": false,
			"id": "qdmdefej",
			"name": "uuid",
			"type": "text",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), edit_uuid); err != nil {
			return err
		}
		collection.Schema.AddField(edit_uuid)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("1l9pedzcwc3pf4x")
		if err != nil {
			return err
		}

		if err := json.Unmarshal([]byte(`[]`), &collection.Indexes); err != nil {
			return err
		}

		// update
		edit_uuid := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
			"system": false,
			"id": "qdmdefej",
			"name": "uuid",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), edit_uuid); err != nil {
			return err
		}
		collection.Schema.AddField(edit_uuid)

		return dao.SaveCollection(collection)
	})
}
