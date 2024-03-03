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
		collection.Schema.RemoveField("u7q9rybb")

		// add
		new_node_id := &schema.SchemaField{}
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
		del_browser_type := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "u7q9rybb",
			"name": "browser_type",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), del_browser_type)
		collection.Schema.AddField(del_browser_type)

		// remove
		collection.Schema.RemoveField("hsw22w9a")

		return dao.SaveCollection(collection)
	})
}
