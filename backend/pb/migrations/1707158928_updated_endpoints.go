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

		collection, err := dao.FindCollectionByNameOrId("33qsslnyye3uscm")
		if err != nil {
			return err
		}

		// add
		new_whitelist := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "8tl038rk",
			"name": "whitelist",
			"type": "json",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"maxSize": 2000000
			}
		}`), new_whitelist)
		collection.Schema.AddField(new_whitelist)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("33qsslnyye3uscm")
		if err != nil {
			return err
		}

		// remove
		collection.Schema.RemoveField("8tl038rk")

		return dao.SaveCollection(collection)
	})
}
