package osquery

import (
	"net/http"

	"github.com/labstack/echo/v5"
)

type EnrollNode struct {
	NodeKey string `json:"node_key"`
}

func Enroll(c echo.Context) error {
	enrollNode := &EnrollNode{
		NodeKey: "this_is_node_key",
	}
	return c.JSON(http.StatusCreated, enrollNode)
}
