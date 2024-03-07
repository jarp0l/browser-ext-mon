import logging

import httpx

from osquery_be.settings import settings
from osquery_be.schemas.config_schemas import (
    ConfigRequest,
    ConfigResponse,
    ConfigResponseSchedule,
)
from osquery_be.osquery.exceptions import InvalidNodeKeyException


def get_config(config_req: ConfigRequest):
    node_key = config_req.node_key

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

        # Since the node_key is valid, we can return the config
        return ConfigResponse(schedule=ConfigResponseSchedule(), node_invalid=False)

    except InvalidNodeKeyException:
        logging.debug("Invalid Node Key.")
        return ConfigResponse(node_invalid=True)

    # If the backend/pb is not running, httpx.ConnectError will be raised
    except httpx.ConnectError:
        logging.error("Is the backend/pb running?")
        return ConfigResponse(node_invalid=True)

    except Exception as exc:
        logging.exception("Unexpected error during getting config.")
        logging.exception(exc)
        return ConfigResponse(node_invalid=True)
