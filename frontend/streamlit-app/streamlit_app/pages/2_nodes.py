import pandas as pd
import streamlit as st

from streamlit_app.utils.apis import get_nodes, get_organization
from streamlit_app.utils.auth_form import LoginForm, auth_form


def populate_page():
    if "bem-email" not in st.session_state:
        return
    admin_email = st.session_state["bem-email"]

    org_data = get_organization(admin_email)
    org_id = org_data["items"][0].get("id")
    if org_id is None:
        st.error("Error fetching organization info!")
        return

    nodes = get_nodes(org_id)
    if nodes is None:
        st.error("Error fetching nodes!")
        return
    if not nodes["totalItems"]:
        st.error("There are no nodes. Run the CLI to add nodes.")
        return

    df = pd.DataFrame(nodes["items"])
    st.data_editor(
        df,
        column_order=(
            "uuid",
            "owner_email",
            "created",
            "updated",
        ),
        column_config={
            "created": "Created",
            "updated": "Updated",
            "owner_email": "Owner Email",
            "uuid": "UUID",
        },
    )


def build_page():
    st.set_page_config(page_title="Nodes", layout="wide")
    st.header("Nodes")
    st.subheader("Showing all nodes")
    if st.sidebar.button("Logout"):
        LoginForm().logout()
    populate_page()


if not LoginForm().is_logged_in():
    auth_form()
else:
    build_page()
