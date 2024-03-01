package osquery

import (
	"net/http"

	"github.com/labstack/echo/v5"
)

type ConfigRequest struct {
	NodeKey string `json:"node_key"`
}

type ConfigResponse struct {
	Schedule    *map[string]ScheduleItem `json:"schedule,omitempty"`
	NodeInvalid bool                     `json:"node_invalid"`
}

type ScheduleItem struct {
	Query    string `json:"query"`
	Interval int    `json:"interval"`
}

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
