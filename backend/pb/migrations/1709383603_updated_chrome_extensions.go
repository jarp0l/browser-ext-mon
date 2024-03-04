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
		new_uid := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "oekeb61q",
			"name": "uid",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_uid)
		collection.Schema.AddField(new_uid)

		// add
		new_name := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "6holmnxw",
			"name": "name",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_name)
		collection.Schema.AddField(new_name)

		// add
		new_profile := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "crzkyzi6",
			"name": "profile",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_profile)
		collection.Schema.AddField(new_profile)

		// add
		new_profile_path := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "ujwhrzwg",
			"name": "profile_path",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_profile_path)
		collection.Schema.AddField(new_profile_path)

		// add
		new_referenced_identifier := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "n5o4nfdd",
			"name": "referenced_identifier",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_referenced_identifier)
		collection.Schema.AddField(new_referenced_identifier)

		// add
		new_identifier := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "zqyp7bms",
			"name": "identifier",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_identifier)
		collection.Schema.AddField(new_identifier)

		// add
		new_version := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "06t3cxto",
			"name": "version",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_version)
		collection.Schema.AddField(new_version)

		// add
		new_description := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "aiobajt3",
			"name": "description",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_description)
		collection.Schema.AddField(new_description)

		// add
		new_default_locale := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "qbdakksj",
			"name": "default_locale",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_default_locale)
		collection.Schema.AddField(new_default_locale)

		// add
		new_current_locale := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "qzyoqhoa",
			"name": "current_locale",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_current_locale)
		collection.Schema.AddField(new_current_locale)

		// add
		new_update_url := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "cz1hkxlq",
			"name": "update_url",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_update_url)
		collection.Schema.AddField(new_update_url)

		// add
		new_author := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "e9lbtphy",
			"name": "author",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_author)
		collection.Schema.AddField(new_author)

		// add
		new_persistent := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "6cwpsswo",
			"name": "persistent",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_persistent)
		collection.Schema.AddField(new_persistent)

		// add
		new_path := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "dnppkmbu",
			"name": "path",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_path)
		collection.Schema.AddField(new_path)

		// add
		new_permissions := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "agspmviy",
			"name": "permissions",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_permissions)
		collection.Schema.AddField(new_permissions)

		// add
		new_permissions_json := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "2homee2a",
			"name": "permissions_json",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_permissions_json)
		collection.Schema.AddField(new_permissions_json)

		// add
		new_optional_permissions := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "gxkv9kwt",
			"name": "optional_permissions",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_optional_permissions)
		collection.Schema.AddField(new_optional_permissions)

		// add
		new_optional_permissions_json := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "re4xq2q4",
			"name": "optional_permissions_json",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_optional_permissions_json)
		collection.Schema.AddField(new_optional_permissions_json)

		// add
		new_manifest_hash := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "rx2o05ta",
			"name": "manifest_hash",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_manifest_hash)
		collection.Schema.AddField(new_manifest_hash)

		// add
		new_referenced := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "vaqugkjc",
			"name": "referenced",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_referenced)
		collection.Schema.AddField(new_referenced)

		// add
		new_from_webstore := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "9cpsedye",
			"name": "from_webstore",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_from_webstore)
		collection.Schema.AddField(new_from_webstore)

		// add
		new_state := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "9h8pmdbr",
			"name": "state",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_state)
		collection.Schema.AddField(new_state)

		// add
		new_install_time := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "ispcn076",
			"name": "install_time",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_install_time)
		collection.Schema.AddField(new_install_time)

		// add
		new_install_timestamp := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "m9ykfzlk",
			"name": "install_timestamp",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_install_timestamp)
		collection.Schema.AddField(new_install_timestamp)

		// add
		new_manifest_json := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "3gtiquem",
			"name": "manifest_json",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_manifest_json)
		collection.Schema.AddField(new_manifest_json)

		// add
		new_key := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "j5lb2zdm",
			"name": "key",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_key)
		collection.Schema.AddField(new_key)

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("67qbz7qdqsebaj2")
		if err != nil {
			return err
		}

		// remove
		collection.Schema.RemoveField("ksn9fd49")

		// remove
		collection.Schema.RemoveField("oekeb61q")

		// remove
		collection.Schema.RemoveField("6holmnxw")

		// remove
		collection.Schema.RemoveField("crzkyzi6")

		// remove
		collection.Schema.RemoveField("ujwhrzwg")

		// remove
		collection.Schema.RemoveField("n5o4nfdd")

		// remove
		collection.Schema.RemoveField("zqyp7bms")

		// remove
		collection.Schema.RemoveField("06t3cxto")

		// remove
		collection.Schema.RemoveField("aiobajt3")

		// remove
		collection.Schema.RemoveField("qbdakksj")

		// remove
		collection.Schema.RemoveField("qzyoqhoa")

		// remove
		collection.Schema.RemoveField("cz1hkxlq")

		// remove
		collection.Schema.RemoveField("e9lbtphy")

		// remove
		collection.Schema.RemoveField("6cwpsswo")

		// remove
		collection.Schema.RemoveField("dnppkmbu")

		// remove
		collection.Schema.RemoveField("agspmviy")

		// remove
		collection.Schema.RemoveField("2homee2a")

		// remove
		collection.Schema.RemoveField("gxkv9kwt")

		// remove
		collection.Schema.RemoveField("re4xq2q4")

		// remove
		collection.Schema.RemoveField("rx2o05ta")

		// remove
		collection.Schema.RemoveField("vaqugkjc")

		// remove
		collection.Schema.RemoveField("9cpsedye")

		// remove
		collection.Schema.RemoveField("9h8pmdbr")

		// remove
		collection.Schema.RemoveField("ispcn076")

		// remove
		collection.Schema.RemoveField("m9ykfzlk")

		// remove
		collection.Schema.RemoveField("3gtiquem")

		// remove
		collection.Schema.RemoveField("j5lb2zdm")

		return dao.SaveCollection(collection)
	})
}
