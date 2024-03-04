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

		if err := json.Unmarshal([]byte(`[
			"CREATE UNIQUE INDEX ` + "`" + `idx_cWkg1kQ` + "`" + ` ON ` + "`" + `organizations` + "`" + ` (` + "`" + `admin_email` + "`" + `)"
		]`), &collection.Indexes); err != nil {
			return err
		}

		// remove
		collection.Schema.RemoveField("2fbbvr3t")

		// add
		new_admin_email := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
			"system": false,
			"id": "beboizpg",
			"name": "admin_email",
			"type": "email",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"exceptDomains": [],
				"onlyDomains": []
			}
		}`), new_admin_email); err != nil {
			return err
		}
		collection.Schema.AddField(new_admin_email)

		// add
		new_api_key := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
			"system": false,
			"id": "p0f1mqtf",
			"name": "api_key",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_api_key); err != nil {
			return err
		}
		collection.Schema.AddField(new_api_key)

		// update
		edit_admin_id := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
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
		}`), edit_admin_id); err != nil {
			return err
		}
		collection.Schema.AddField(edit_admin_id)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("bxllu29bavy3izv")
		if err != nil {
			return err
		}

		if err := json.Unmarshal([]byte(`[
			"CREATE UNIQUE INDEX ` + "`" + `idx_G9dh1kY` + "`" + ` ON ` + "`" + `organizations` + "`" + ` (` + "`" + `slug` + "`" + `)"
		]`), &collection.Indexes); err != nil {
			return err
		}

		// add
		del_slug := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
			"system": false,
			"id": "2fbbvr3t",
			"name": "slug",
			"type": "text",
			"required": true,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), del_slug); err != nil {
			return err
		}
		collection.Schema.AddField(del_slug)

		// remove
		collection.Schema.RemoveField("beboizpg")

		// remove
		collection.Schema.RemoveField("p0f1mqtf")

		// update
		edit_admin_id := &schema.SchemaField{}
		if err := json.Unmarshal([]byte(`{
			"system": false,
			"id": "75ahp2qq",
			"name": "admin",
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
		}`), edit_admin_id); err != nil {
			return err
		}
		collection.Schema.AddField(edit_admin_id)

		return dao.SaveCollection(collection)
	})
}
