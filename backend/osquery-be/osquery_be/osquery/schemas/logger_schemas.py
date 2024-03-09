from typing import Optional

from pydantic import BaseModel

from osquery_be.osquery.schemas.common_schemas import LogType, LogTypeResult, LogTypeStatus
from osquery_be.osquery.schemas.config_schemas import ConfigRequest


class LoggerRequest(ConfigRequest):
    data: Optional[list[LogTypeStatus | LogTypeResult]] = []
    log_type: Optional[LogType] = LogType.STATUS
    node_key: str

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "data": [
                        {
                            "name": "frefox_addons",
                            "hostIdentifier": "6d0481b2-fd6d-435f-80bc-564a8736dd56",
                            "calendarTime": "Mon Apr 1 13:33:37 2024 UTC",
                            "unixTime": 1711957717,
                            "epoch": 0,
                            "counter": 0,
                            "numerics": False,
                            "columns": {
                                "active": "0",
                                "autoupdate": "1",
                                "creator": "null",
                                "description": "",
                                "disabled": "1",
                                "identifier": "{12eeb304-58cd-4bcb-9676-99562b04f066}",
                                "location": "app-profile",
                                "name": "Catppuccin-mocha-sky",
                                "path": "/Users/abc/Library/Application Support/Firefox/Profiles/12233344.default-release/extensions/{12eeb304-58cd-4bcb-9676-99562b04f066}.xpi",
                                "source_url": "https://addons.mozilla.org/firefox/downloads/file/3954372/catppuccin_dark_sky-2.0.xpi",
                                "type": "theme",
                                "uid": "501",
                                "version": "2.0",
                                "visible": "1",
                            },
                            "action": "added",
                        },
                    ],
                    "log_type": "result",
                    "node_key": "6d0481b2-fd6d-435f-80bc-564a8736dd56",
                },
                {
                    "data": [
                        {
                            "hostIdentifier": "6d0481b2-fd6d-435f-80bc-564a8736dd56",
                            "calendarTime": "Mon Apr 1 13:33:37 2024 UTC",
                            "unixTime": 1711957717,
                            "severity": 2,
                            "filename": "init.cpp",
                            "line": 714,
                            "message": "An error occurred during extension manager startup: Cannot create extension socket: /var/osquery/osquery.em",
                            "version": "5.11.0",
                        }
                    ],
                    "log_type": "status",
                    "node_key": "6d0481b2-fd6d-435f-80bc-564a8736dd56",
                },
            ]
        }
    }


class LoggerResponse(BaseModel):
    node_invalid: bool = False
