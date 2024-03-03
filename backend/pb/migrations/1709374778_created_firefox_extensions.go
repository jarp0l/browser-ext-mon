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
			"id": "d0lxxvunn80r1ye",
			"created": "2024-03-02 10:19:38.824Z",
			"updated": "2024-03-02 10:19:38.824Z",
			"name": "firefox_extensions",
			"type": "base",
			"system": false,
			"schema": [
				{
					"system": false,
					"id": "mvgnszzg",
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

		collection, err := dao.FindCollectionByNameOrId("d0lxxvunn80r1ye")
		if err != nil {
			return err
		}

		return dao.DeleteCollection(collection)
	})
}
