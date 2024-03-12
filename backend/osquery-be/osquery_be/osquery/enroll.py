import json
import logging

import httpx
from osquery_be.settings import settings
from osquery_be.osquery.schemas.enroll_schemas import (
    EnrollRequest,
    EnrollResponse,
    EnrollSecret,
)
from osquery_be.osquery.exceptions import InvalidAPIKeyException


def enroll_node(enroll_req: EnrollRequest):
    enroll_secret = json.loads(enroll_req.enroll_secret)
    enroll_secret_model = EnrollSecret(**enroll_secret)
    api_key = enroll_secret_model.api_key
    owner_email = enroll_secret_model.owner_email
    host_identifier = enroll_req.host_identifier

    headers = {
        "X-SERVICE-TOKEN": settings.service_token,
    }

    try:
        client = httpx.Client()

        # Check if the api_key is valid
        search_orgs = client.get(
            f"{settings.pb_api_url}/collections/organizations/records",
            headers=headers,
            params={"filter": f"(api_key='{api_key}')"},
        ).json()

        # If api_key belongs to any organization, totalItems will be 1
        if search_orgs["totalItems"] != 1:
            raise InvalidAPIKeyException

        # Check if the node is already enrolled
        search_nodes = client.get(
            f"{settings.pb_api_url}/collections/nodes/records",
            headers=headers,
            params={"filter": f"(uuid='{host_identifier}')"},
        ).json()

        # If node is already enrolled, totalItems will be 1
        if search_nodes["totalItems"] != 1:
            # Create a new node since there is no node with the given host_identifier/uuid
            _ = client.post(
                f"{settings.pb_api_url}/collections/nodes/records",
                headers=headers,
                json={
                    "uuid": host_identifier,
                    "org_id": search_orgs["items"][0]["id"],
                    "owner_email": owner_email,
                },
            ).json()
        return EnrollResponse(node_key=host_identifier, node_invalid=False)

    except InvalidAPIKeyException:
        logging.debug("Invalid API Key.")
        return EnrollResponse(node_invalid=True)

    # If the backend/pb is not running, httpx.ConnectError will be raised
    except httpx.ConnectError:
        logging.error("Is the backend/pb running?")
        return EnrollResponse(node_invalid=True)

    except Exception as exc:
        logging.exception("Unexpected error during enrollment.")
        logging.exception(exc)
        return EnrollResponse(node_invalid=True)
