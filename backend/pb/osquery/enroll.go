package osquery

import (
	"net/http"

	"github.com/labstack/echo/v5"
)

type EnrollRequest struct {
	APIKey       string `json:"api_key"`
	OwnerEmail   string `json:"owner_email"`
}

type EnrollResponse struct {
	NodeKey     string `json:"node_key"`	// TODO: if API key is valid, hash and salt org_id and return as node_key
	NodeInvalid bool   `json:"node_invalid"`
}

func Enroll(c echo.Context) error {
	enrollRes := &EnrollResponse{
		NodeKey: "this_is_node_key",
	}
	enrollReq := new(EnrollRequest)
	if err := c.Bind(enrollReq); err != nil {
		return c.String(http.StatusBadRequest, err.Error())
	}
	return c.JSON(http.StatusCreated, enrollRes)
}
