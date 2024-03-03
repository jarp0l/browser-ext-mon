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

		collection, err := dao.FindCollectionByNameOrId("d0lxxvunn80r1ye")
		if err != nil {
			return err
		}

		// add
		new_uid := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "rwwdvjbn",
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
			"id": "nn2nmbno",
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
		new_identifier := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "jculoat1",
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
		new_creator := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "2qewdshj",
			"name": "creator",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_creator)
		collection.Schema.AddField(new_creator)

		// add
		new_type := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "576qyi5x",
			"name": "type",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_type)
		collection.Schema.AddField(new_type)

		// add
		new_version := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "xfjaq5hh",
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
			"id": "adqhmx9d",
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
		new_source_url := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "vohhsxkf",
			"name": "source_url",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_source_url)
		collection.Schema.AddField(new_source_url)

		// add
		new_visible := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "te5sjohr",
			"name": "visible",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_visible)
		collection.Schema.AddField(new_visible)

		// add
		new_active := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "lu1fibid",
			"name": "active",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_active)
		collection.Schema.AddField(new_active)

		// add
		new_disabled := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "rorresui",
			"name": "disabled",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_disabled)
		collection.Schema.AddField(new_disabled)

		// add
		new_autoupdate := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "bevctzwo",
			"name": "autoupdate",
			"type": "number",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"noDecimal": false
			}
		}`), new_autoupdate)
		collection.Schema.AddField(new_autoupdate)

		// add
		new_location := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "bxwie67m",
			"name": "location",
			"type": "text",
			"required": false,
			"presentable": false,
			"unique": false,
			"options": {
				"min": null,
				"max": null,
				"pattern": ""
			}
		}`), new_location)
		collection.Schema.AddField(new_location)

		// add
		new_path := &schema.SchemaField{}
		json.Unmarshal([]byte(`{
			"system": false,
			"id": "xgzerzfx",
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

		return dao.SaveCollection(collection)
	}, func(db dbx.Builder) error {
		dao := daos.New(db);

		collection, err := dao.FindCollectionByNameOrId("d0lxxvunn80r1ye")
		if err != nil {
			return err
		}

		// remove
		collection.Schema.RemoveField("rwwdvjbn")

		// remove
		collection.Schema.RemoveField("nn2nmbno")

		// remove
		collection.Schema.RemoveField("jculoat1")

		// remove
		collection.Schema.RemoveField("2qewdshj")

		// remove
		collection.Schema.RemoveField("576qyi5x")

		// remove
		collection.Schema.RemoveField("xfjaq5hh")

		// remove
		collection.Schema.RemoveField("adqhmx9d")

		// remove
		collection.Schema.RemoveField("vohhsxkf")

		// remove
		collection.Schema.RemoveField("te5sjohr")

		// remove
		collection.Schema.RemoveField("lu1fibid")

		// remove
		collection.Schema.RemoveField("rorresui")

		// remove
		collection.Schema.RemoveField("bevctzwo")

		// remove
		collection.Schema.RemoveField("bxwie67m")

		// remove
		collection.Schema.RemoveField("xgzerzfx")

		return dao.SaveCollection(collection)
	})
}
