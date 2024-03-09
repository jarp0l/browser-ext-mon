from typing import Annotated, Optional

from pydantic import BaseModel
from osquery_be.osquery.schemas.common_schemas import LogTypeStatus, LogType


class ConfigRequest(BaseModel):
    data: Optional[list[LogTypeStatus]] = []
    log_type: Optional[LogType] = LogType.STATUS
    node_key: str

    model_config = {
        "json_schema_extra": {
            "examples": [
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
                }
            ]
        }
    }


class ConfigResponseOptions(BaseModel):
    host_identifier: Annotated[str, "We use uuid as host identifier"] = "uuid"


class ConfigResponseScheduleFirefox(BaseModel):
    query: Annotated[
        str,
        "Query to run on nodes",
    ] = "select * from firefox_addons where source_url<>'null';"
    interval: Annotated[int, "Interval to run the query (in seconds)"] = 30


class ConfigResponseScheduleChrome(BaseModel):
    query: Annotated[
        str,
        "Query to run on nodes",
    ] = "select * from chrome_extensions;"
    interval: Annotated[int, "Interval to run the query (in seconds)"] = 30


class ConfigResponseSchedule(BaseModel):
    """For `schedule` key in ConfigResponse.

    This is a nested model. If you want to add scheduled queries for other browsers,
    or even remove the queries, you have to add/remove here. In case you are adding,
    make sure the models have been added above.
    """

    firefox_addons: Optional[
        ConfigResponseScheduleFirefox
    ] = ConfigResponseScheduleFirefox()
    chrome_extensions: Optional[
        ConfigResponseScheduleChrome
    ] = ConfigResponseScheduleChrome()


class ConfigResponse(BaseModel):
    options: Optional[ConfigResponseOptions] = ConfigResponseOptions()
    schedule: Optional[ConfigResponseSchedule] = {}
    node_invalid: bool = False

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "options": {"host_identifier": "uuid"},
                    "schedule": {
                        "firefox_addons": {
                            "query": "select * from firefox_addons where source_url<>'null' limit 2;",
                            "interval": 5,
                        },
                        "chrome_extensions": {
                            "query": "select * from chrome_extensions limit 2;",
                            "interval": 5,
                        },
                    },
                    "node_invalid": False,
                }
            ]
        }
    }
