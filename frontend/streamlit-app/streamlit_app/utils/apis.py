import logging
import os
import streamlit as st
import httpx

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8090/api")


def make_get_request(collection, filter):
    try:
        res = httpx.get(
            f"{API_BASE_URL}/collections/{collection}/records",
            params={"filter": filter},
        )
        if res.status_code == 200:
            return res.json()
        elif res.status_code in [400, 403]:
            logging.error(res.json())
            return None
    except Exception as e:
        logging.error(e)
        return None


def get_nodes(org_id):
    if "nodes" in st.session_state:
        return st.session_state["nodes"]
    nodes = make_get_request("nodes", filter=f"(org_id='{org_id}')")
    if nodes is not None:
        st.session_state["nodes"] = nodes
    return nodes


def get_extensions(collection, node_id):
    extension_node = make_get_request(
        collection=collection, filter=f"(node_id='{node_id}')"
    )
    return extension_node
