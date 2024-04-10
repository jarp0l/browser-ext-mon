import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

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
        chrome_df = pd.DataFrame(
            [
                extension
                for extension in all_chrome_extensions
                if extension.get("browser_type") == "chrome"
            ]
        )
        brave_df = pd.DataFrame(
            [
                extension
                for extension in all_chrome_extensions
                if extension.get("browser_type") == "braver"
            ]
        )

    grid_options = {
        "autoSizeStrategy": {"type": "fitCellContents"},
        "rowSelection": "single",
        "defaultColDef": {
            "filter": "agTextColumnFilter",
            "floatingFilter": True,
            "cellStyle": {"line-height": "32px"},
        },
        "rowHeight": 36,
        "pagination": True,
        "paginationPageSize": 10,
        "paginationPageSizeSelector": [10, 25, 50],
        "alwaysShowHorizontalScroll": True,
        "alwaysShowVerticalScroll": True,
    }

    # alternative to dynamically adjust tabs
    # problem is the tab indexing has to be adopted as per this approach
    # st.tabs(
    #     [
    #         name
    #         for (name, df) in [
    #             ("Firefox", firefox_df),
    #             ("Chrome", chrome_df),
    #             ("Brave", brave_df),
    #         ]
    #         if not df.empty
    #     ]
    # )

    tabs = st.tabs(["Firefox", "Chrome", "Brave"])
    with tabs[0]:
        st.subheader("Firefox Extensions")

        firefox_grid_options = {
            "columnDefs": [
                {
                    "field": "name",
                    "cellRenderer": "agGroupCellRenderer",
                    "checkboxSelection": True,
                },
                {"field": "version"},
                {"field": "identifier"},
                {"field": "description"},
                {"field": "creator"},
                {"field": "node_id"},
                {"field": "active"},
                {"field": "disabled"},
                {"field": "path"},
            ],
            "rowData": firefox_df.to_dict("records"),
        }
        grid_options.update(firefox_grid_options)
        firefox_grid = AgGrid(
            None,
            gridOptions=grid_options,
            allow_unsafe_jscode=True,
            key="firefox_grid",
            theme="streamlit",
        )

    def chrome_grid_options(browser_type):
        return {
            "columnDefs": [
                {
                    "field": "name",
                    "cellRenderer": "agGroupCellRenderer",
                    "checkboxSelection": True,
                },
                {"field": "version"},
                {"field": "identifier"},
                {"field": "description"},
                {"field": "author"},
                {"field": "node_id"},
                {"field": "permissions"},
                {"field": "optional_permissions"},
                {"field": "profile_path"},
            ],
            "rowData": browser_type.to_dict("records"),
        }

    with tabs[1]:
        st.subheader("Chrome Extensions")

        grid_options.update(chrome_grid_options(chrome_df))
        chrome_grid = AgGrid(
            None,
            gridOptions=grid_options,
            allow_unsafe_jscode=True,
            key="chrome_grid",
            theme="streamlit",
        )

    with tabs[2]:
        st.subheader("Brave Extensions")

        grid_options.update(chrome_grid_options(brave_df))
        brave_grid = AgGrid(
            None,
            gridOptions=grid_options,
            allow_unsafe_jscode=True,
            key="brave_grid",
            theme="streamlit",
        )

    try:
        selected_row = (
            firefox_grid.selected_rows_id
            or chrome_grid.selected_rows_id
            or brave_grid.selected_rows_id
        )
        with st.container(border=True):
            st.subheader("Scan Results")

            if selected_row and firefox_grid.selected_rows_id:
                selected_extension = pd.json_normalize(
                    firefox_df.iloc[selected_row].to_dict(orient="records")
                )
                st.write("Firefox Extension: " + selected_extension["name"][0])

            if selected_row and brave_grid.selected_rows_id:
                selected_extension = brave_df.iloc[selected_row]
                "Brave Extension"
                selected_extension

            if selected_row and chrome_grid.selected_rows_id:
                selected_extension = chrome_df.iloc[selected_row]
                "Chrome Extension"
                selected_extension
    except Exception:
        pass


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
