import json
import logging
import os

import httpx

from osquery_be.schemas import EnrollRequest, EnrollResponse
from osquery_be.utils.exceptions import InvalidAPIKeyException

# host.docker.internal is a special DNS name which resolves to the internal IP address used by the host
# We need this to connect to backen/pb instance running on the host machine
PB_API_URL = os.getenv("PB_API_DOCKER_URL", "http://localhost:8090/api")
SERVICE_TOKEN = os.getenv("PB_OSQUERY_SERVICE_TOKEN", "osquery-be")


def enroll_node(enroll_request: EnrollRequest):
    enroll_secret = json.loads(enroll_request.enroll_secret)
    api_key = enroll_secret["api_key"]
    owner_email = enroll_secret["owner_email"]
    host_identifier = enroll_request.host_identifier

    headers = {
        "X-SERVICE-TOKEN": SERVICE_TOKEN,
    }

    try:
        client = httpx.Client()

        # Check if the api_key is valid
        search_orgs = client.get(
            f"{PB_API_URL}/collections/organizations/records",
            headers=headers,
            params={"filter": f"(api_key='{api_key}')"},
        ).json()

        # If api_key belongs to any organization, totalItems will be 1
        if search_orgs["totalItems"] != 1:
            raise InvalidAPIKeyException

        # Check if the node is already enrolled
        search_nodes = client.get(
            f"{PB_API_URL}/collections/nodes/records",
            headers=headers,
            params={"filter": f"(uuid='{host_identifier}')"},
        ).json()

        # If node is already enrolled, totalItems will be 1
        if search_nodes["totalItems"] != 1:
            # Create a new node since there is no node with the given host_identifier/uuid
            _ = client.post(
                f"{PB_API_URL}/collections/nodes/records",
                headers=headers,
                json={
                    "uuid": host_identifier,
                    "org_id": search_orgs["items"][0]["id"],
                    "owner_email": owner_email,
                },
            ).json()
        return EnrollResponse(node_key=host_identifier)

    except InvalidAPIKeyException:
        logging.exception("Invalid API Key")
        return EnrollResponse(node_key="")

    except Exception as exc:
        logging.exception("Unexpected error during enrollment")
        logging.exception(exc)
        return EnrollResponse(node_key="")
