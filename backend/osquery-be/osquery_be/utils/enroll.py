import os
import logging
import httpx
from osquery_be.schemas import EnrollRequestSchema

PB_API_URL = os.getenv("PB_API_URL", "http://localhost:8090/api")
SERVICE_TOKEN = os.getenv("PB_OSQUERY_SERVICE_TOKEN", "osquery-be")


def enroll_node(enroll_req: EnrollRequestSchema):
    enroll_secret = enroll_req.enroll_secret
    api_key = enroll_secret["api_key"]
    owner_email = enroll_secret["owner_email"]
    host_identifier = enroll_req.host_identifier

    headers = {
        "X-SERVICE-TOKEN": SERVICE_TOKEN,
    }

    session = httpx.Session()
    try:
        search_orgs = session.get(
            f"{PB_API_URL}/collections/organizations/records",
            headers=headers,
            params={"filter": f"(api_key='{api_key}')"},
        )
        search_orgs = search_orgs.json()
        if search_orgs["totalItems"] != 1:
            return {}

        search_nodes = session.get(
            f"{PB_API_URL}/collections/nodes/records",
            headers=headers,
            params={"filter": f"(uuid='{host_identifier}')"},
        )
        search_nodes = search_nodes.json()
        if search_nodes["totalItems"] != 1:
            create_node = session.post(
                f"{PB_API_URL}/collections/nodes/records",
                headers=headers,
                body={
                    "uuid": host_identifier,
                    "org_id": search_orgs["items"]["id"],
                    "owner_email": owner_email,
                },
            )
            create_node = create_node.json()

    except Exception as exc:
        logging.exception(exc)
        return {}

    return


def enroll(api_key):
    url = f"{PB_API_URL}/collections/organizations/records"
    headers = {
        "X-SERVICE-TOKEN": SERVICE_TOKEN,
    }
    params = {"filter": f"(api_key='{api_key}')"}

    try:
        response = httpx.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        return data["totalItems"]

    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

    return None


def test_endpoint(org_id):
    # Example of testing an endpoint with the organization ID
    url = f"{PB_API_URL}/collections/nodes/records"
    params = {"filter": f"(uuid='{uuid}')"}
    headers = {
        "X-SERVICE-TOKEN": SERVICE_TOKEN,
    }
    response = httpx.get(url, headers=headers, params=params)
    try:
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        for item in items:
            print("Collection ID:", item.get("collectionId"))
            print("Collection Name:", item.get("collectionName"))
            print("Created:", item.get("created"))
            print("ID:", item.get("id"))
            print("Org ID:", item.get("org_id"))
            print("Owner Email:", item.get("owner_email"))
            print("Updated:", item.get("updated"))
            print("UUID:", item.get("uuid"))
            print()
        return data["totalItems"]
        # Process data from the endpoint
        print("Response from endpoint:")
        print(data)
    except httpx.HTTPStatusError as e:
        print(f"HTTP error occurred: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Example usage
    api_key = "mW9oUTfiryOJvZPX"
    uuid = "fdsa"

    # org_id = enroll(api_key)
    total_org_item = enroll(api_key)
    if total_org_item > 0:
        total_node_item = test_endpoint(uuid)
        if total_node_item > 0:
            print(total_node_item)

    else:
        print("organization does not exist")
