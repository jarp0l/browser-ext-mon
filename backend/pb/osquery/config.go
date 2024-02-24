package osquery

import (
	"net/http"

	"github.com/labstack/echo/v5"
)

func GetConfig(c echo.Context) error {
	return c.JSON(http.StatusOK, map[string]interface{}{
		"config": map[string]interface{}{
			"logger_path": "/var/log/osquery",
			"config_path": "/etc/osquery/osquery.conf",
		},
	})
}

func PostConfig(c echo.Context) error {
	return c.JSON(http.StatusCreated, map[string]interface{}{
		"success": true,
	})
}
