package migrations

import (
	"encoding/json"

	"github.com/pocketbase/dbx"
	"github.com/pocketbase/pocketbase/daos"
	m "github.com/pocketbase/pocketbase/migrations"
	"github.com/pocketbase/pocketbase/models"
)

func init() {
	m.Register(func(db dbx.Builder) error {
		jsonData := `{
			"id": "67qbz7qdqsebaj2",
			"created": "2024-03-02 12:13:23.132Z",
			"updated": "2024-03-02 12:13:23.132Z",
			"name": "chrome_extensions",
			"type": "base",
			"system": false,
			"schema": [
				{
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
				}
			],
			"indexes": [],
			"listRule": null,
			"viewRule": null,
			"createRule": null,
			"updateRule": null,
			"deleteRule": null,
			"options": {}
		}`

		collection := &models.Collection{}
		if err := json.Unmarshal([]byte(jsonData), &collection); err != nil {
			return err
		}

		return daos.New(db).SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("67qbz7qdqsebaj2")
		if err != nil {
			return err
		}

		return dao.DeleteCollection(collection)
	})
}
