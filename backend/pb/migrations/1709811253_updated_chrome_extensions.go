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

		collection, err := dao.FindCollectionByNameOrId("67qbz7qdqsebaj2")
		if err != nil {
			return err
		}

		// add
		new_node_id := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
			"system": false,
			"id": "qc8gmmel",
			"name": "node_id",
			"type": "relation",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"collectionId": "1l9pedzcwc3pf4x",
				"cascadeDelete": true,
				"minSelect": null,
				"maxSelect": 1,
				"displayFields": null
			}
		}`), new_node_id); err != nil {
			return err
		}
		collection.Schema.AddField(new_node_id)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("67qbz7qdqsebaj2")
		if err != nil {
			return err
		}

		// remove
		collection.Schema.RemoveField("qc8gmmel")

		return dao.SaveCollection(collection)
	})
}
