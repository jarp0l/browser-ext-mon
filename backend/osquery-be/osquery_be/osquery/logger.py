import logging

import httpx

from osquery_be.osquery.exceptions import (
    InvalidNodeKeyException,
    NodeNotFoundException,
    NothingToDoException,
)
from osquery_be.schemas.common_schemas import LogType
from osquery_be.schemas.logger_schemas import LoggerRequest, LoggerResponse
from osquery_be.settings import settings


def store_logs(logger_req: LoggerRequest):
    node_key = logger_req.node_key

    headers = {
        "X-SERVICE-TOKEN": settings.service_token,
    }

    try:
        client = httpx.Client()

        # Check if the node_key is valid
        search_nodes = client.get(
            f"{settings.pb_api_url}/collections/nodes/records",
            headers=headers,
            params={"filter": f"(uuid='{node_key}')"},
        ).json()  # current assumption is uuid == node_key

        # If node_key belongs to any node, totalItems will be 1
        if search_nodes["totalItems"] != 1:
            raise InvalidNodeKeyException

        # We only want to process 'result' logs, and ignore 'status' logs
        # 'result' logs => response from config endpoint which contains the query results
        # 'status' logs => response which, in general, contains the status and any erros of the osquery agent
        log_type = logger_req.log_type
        if log_type != LogType.RESULT:
            raise NothingToDoException

        # If there is nothing else wrong, just store logs in DB.
        # There is a constraint on DB that *both* node_id && identifier must be unique for successful insertion.
        # So there is no need to check that here.
        node_id = search_nodes["items"][0]["id"]
        for log_data in logger_req.data:
            if log_data.name == "firefox_addons":  # name of the scheduled_query
                _ = client.post(
                    f"{settings.pb_api_url}/collections/firefox_extensions/records",
                    headers=headers,
                    json={
                        "node_id": node_id,
                        "uid": int(log_data.columns.uid),
                        "name": log_data.columns.name,
                        "identifier": log_data.columns.identifier,
                        "creator": log_data.columns.creator,
                        "type": log_data.columns.type_,
                        "version": log_data.columns.version,
                        "description": log_data.columns.description,
                        "source_url": log_data.columns.source_url,
                        "visible": int(log_data.columns.visible),
                        "active": int(log_data.columns.active),
                        "disabled": int(log_data.columns.disabled),
                        "autoupdate": int(log_data.columns.autoupdate),
                        "location": log_data.columns.location,
                        "path": log_data.columns.path,
                    },
                ).json()

            if log_data.name == "chrome_extensions":
                _ = client.post(
                    f"{settings.pb_api_url}/collections/chrome_extensions/records",
                    headers=headers,
                    json={
                        "node_id": node_id,
                        "browser_type": log_data.columns.browser_type,
                        "uid": int(log_data.columns.uid),
                        "name": log_data.columns.name,
                        "profile": log_data.columns.profile,
                        "profile_path": log_data.columns.profile_path,
                        "referenced_identifier": log_data.columns.referenced_identifier,
                        "identifier": log_data.columns.identifier,
                        "version": log_data.columns.version,
                        "description": log_data.columns.description,
                        "default_locale": log_data.columns.default_locale,
                        "current_locale": log_data.columns.current_locale,
                        "update_url": log_data.columns.update_url,
                        "author": log_data.columns.author,
                        "persistent": int(log_data.columns.persistent),
                        "path": log_data.columns.path,
                        "permissions": log_data.columns.permissions,
                        "permissions_json": log_data.columns.permissions_json,
                        "optional_permissions": log_data.columns.optional_permissions,
                        "optional_permissions_json": log_data.columns.optional_permissions_json,
                        "manifest_hash": log_data.columns.manifest_hash,
                        "referenced": int(log_data.columns.referenced),
                        "from_webstore": log_data.columns.from_webstore,
                        "state": log_data.columns.state,
                        "install_time": log_data.columns.install_time,
                        "install_timestamp": int(log_data.columns.install_timestamp),
                        "manifest_json": log_data.columns.manifest_json,
                        "key": log_data.columns.key,
                    },
                ).json()
        return LoggerResponse(node_invalid=False)

    except NothingToDoException:
        logging.debug("log_type is 'status'. Nothing to do.")
        return LoggerResponse(node_invalid=False)  # node is still valid

    except InvalidNodeKeyException:
        logging.debug("Invalid Node Key.")
        return LoggerResponse(node_invalid=True)

    except NodeNotFoundException:
        logging.debug("Node not found.")
        return LoggerResponse(node_invalid=True)

    # If the backend/pb is not running, httpx.ConnectError will be raised
    except httpx.ConnectError:
        logging.error("Is the backend/pb running?")
        return LoggerResponse(node_invalid=True)

    except Exception as exc:
        logging.exception("Unexpected error during getting config.")
        logging.exception(exc)
        return LoggerResponse(node_invalid=True)