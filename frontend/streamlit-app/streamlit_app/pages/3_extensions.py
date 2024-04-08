import pandas as pd
import streamlit as st

from streamlit_app.utils.apis import get_extensions, get_nodes, get_organization
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

    all_firefox_extensions = []
    all_chrome_extensions = []
    for node in nodes["items"]:
        firefox_extensions = get_extensions("firefox_extensions", node.get("id"))
        chrome_extensions = get_extensions("chrome_extensions", node.get("id"))
        if firefox_extensions is None:
            st.error("Error fetching firefox extensions!")
            return
        if chrome_extensions is None:
            st.error("Error fetching chrome extensions!")
            return
        all_firefox_extensions.extend(firefox_extensions["items"])
        all_chrome_extensions.extend(chrome_extensions["items"])

        firefox_df = pd.DataFrame(all_firefox_extensions)
        chrome_df = pd.DataFrame(all_chrome_extensions)

    with st.container(border=True):
        st.subheader("Firefox Extensions")
        st.data_editor(
            firefox_df,
            column_order=(
                "name",
                "version",
                "identifier",
                "description",
                "creator",
                "node_id",
                "active",
                "disabled",
                "path",
            ),
            column_config={
                "active": st.column_config.CheckboxColumn("Enabled?", disabled=True),
                "disabled": st.column_config.CheckboxColumn("Disabled?", disabled=True),
                "creator": "Creator",
                "description": "Description",
                "identifier": "Identifier",
                "name": "Name",
                "node_id": "Node ID",
                "path": "Path",
                "uid": "UID",
                "version": "Version",
            },
        )

    with st.container(border=True):
        st.subheader("Chrome Extensions")
        st.data_editor(
            chrome_df,
            column_order=(
                "name",
                "version",
                "referenced_identifier",
                "description",
                "author",
                "browser_type",
                "node_id",
                "permissions",
                "optional_permissions",
                "manifest_hash",
                "profile_path",
                "from_webstore",
            ),
            column_config={
                "name": "Name",
                "version": "Version",
                "referenced_identifier": "Identifier",
                "description": "Description",
                "author": "Author",
                "browser_type": "Browser Type",
                "node_id": "Node ID",
                "permissions": "Permissions",
                "optional_permissions": "Optional Permissions",
                "manifest_hash": "Manifest Hash",
                "profile_path": "Profile Path",
                "from_webstore": st.column_config.CheckboxColumn(
                    "From Webstore?", disabled=True
                ),
            },
        )


def build_page():
    st.set_page_config(page_title="Extensions", layout="wide")
    st.header("Extensions")

    if st.sidebar.button("Logout"):
        LoginForm().logout()

    populate_page()


if not LoginForm().is_logged_in():
    auth_form()
else:
    build_page()
