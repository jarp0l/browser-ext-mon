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

		// remove
		collection.Schema.RemoveField("hsw22w9a")

		// add
		new_node_id := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "audn6vhj",
			"name": "node_id",
			"type": "relation",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"collectionId": "1l9pedzcwc3pf4x",
				"cascadeDelete": false,
				"minSelect": null,
				"maxSelect": 1,
				"displayFields": null
			}
		}`), new_node_id)
		collection.Schema.AddField(new_node_id)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("67qbz7qdqsebaj2")
		if err != nil {
			return err
		}

		// add
		del_node_id := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "hsw22w9a",
			"name": "node_id",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), del_node_id)
		collection.Schema.AddField(del_node_id)

		// remove
		collection.Schema.RemoveField("audn6vhj")

		return dao.SaveCollection(collection)
	})
}
