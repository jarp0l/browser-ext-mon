import pandas as pd
import streamlit as st

from streamlit_app.utils.apis import get_extensions, get_nodes
from streamlit_app.utils.auth_form import LoginForm, auth_form


def populate_page():
    st.subheader("List of firefox extensions")
    org_id = "72b53p7ai8s9wdm"
    data_node = get_nodes(org_id)

    item_node = data_node["items"]

    for item in item_node:
        extension_firefox_node = get_extensions("firefox_extensions", item.get("id"))
        if extension_firefox_node is None:
            st.error("error fetching extension records")
            return
        if extension_firefox_node["totalItems"]:
            df = pd.DataFrame(extension_firefox_node["items"])
            st.data_editor(df)
        else:
            st.error("total items in node is zero")

        total_item1 = extension_firefox_node["totalItems"]

    st.subheader("list of chrome extensions")
    for item in item_node:
        extension_chrome_node = get_extensions("chrome_extensions", item.get("id"))
        if extension_chrome_node is None:
            st.error("error fetching extension records")
            return
        if extension_chrome_node["totalItems"]:
            df = pd.DataFrame(extension_chrome_node["items"])
            st.data_editor(df)
        else:
            st.error("total items in node is zero")

        total_item2 = extension_chrome_node["totalItems"]

    all_extensions = df["identifier"].value_counts().reset_index()
    all_extensions.columns = ["identifier", "count"]
    top_5_extensions = all_extensions.head(5)

    # Display the top 5 extensions in a bar chart
    st.subheader("Top 5 Most Used Extensions")
    st.bar_chart(top_5_extensions.set_index("identifier"))
    total_extensions = total_item1 + total_item2
    st.write(total_extensions)


def build_page():
    st.set_page_config(page_title="Extensions")
    st.header("Extensions")

    if st.sidebar.button("Logout"):
        LoginForm().logout()

    populate_page()


if not LoginForm().is_logged_in():
    auth_form()
else:
    build_page()
