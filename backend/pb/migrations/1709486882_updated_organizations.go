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

		json.Unmarshal([]byte(`[
			"CREATE UNIQUE INDEX ` + "`" + `idx_YoPSpsT` + "`" + ` ON ` + "`" + `organizations` + "`" + ` (` + "`" + `admin_email` + "`" + `)"
		]`), &collection.Indexes)

		// add
		new_admin_email := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "htqusstv",
			"name": "admin_email",
			"type": "email",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"exceptDomains": [],
				"onlyDomains": []
			}
		}`), new_admin_email)
		collection.Schema.AddField(new_admin_email)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("bxllu29bavy3izv")
		if err != nil {
			return err
		}

		json.Unmarshal([]byte(`[]`), &collection.Indexes)

		// remove
		collection.Schema.RemoveField("htqusstv")

		return dao.SaveCollection(collection)
	})
}
