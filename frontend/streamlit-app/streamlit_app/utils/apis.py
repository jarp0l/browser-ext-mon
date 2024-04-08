import logging
import os

import httpx

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8090/api")


def make_get_request(collection, filter):
    try:
        res = httpx.get(
            f"{API_BASE_URL}/collections/{collection}/records",
            params={"filter": filter},
            headers={"X-SERVICE-TOKEN": "streamlit-app"},
        )
        if res.status_code == 200:
            return res.json()
        elif res.status_code in [400, 403]:
            logging.error(res.json())
            return None
    except Exception as e:
        logging.error(e)
        return None


def get_organization(admin_email):
    org_data = make_get_request(
        collection="organizations", filter=f"(admin_email='{admin_email}')"
    )
    if org_data is None:
        return None
    return org_data


def get_nodes(org_id):
    nodes = make_get_request("nodes", filter=f"(org_id='{org_id}')")
    if nodes is None:
        return None
    return nodes


def get_extensions(collection, node_id):
    extension_node = make_get_request(
        collection=collection, filter=f"(node_id='{node_id}')"
    )
    return extension_node
