import streamlit as st

from streamlit_app.utils.apis import get_extensions, get_nodes, get_organization
from streamlit_app.utils.auth_form import LoginForm, auth_form


def populate_page():
    if "bem-email" not in st.session_state:
        return
    admin_email = st.session_state["bem-email"]

    org = get_organization(admin_email)
    api_key = org["items"][0].get("api_key")
    org_id = org["items"][0].get("id")
    if api_key is None:
        st.error("Error fetching organization info!")
        return

    nodes = get_nodes(org_id)
    if nodes is None:
        st.error("Error fetching nodes!")
        return

    total_extensions = 0
    for node in nodes["items"]:
        firefox_extensions = get_extensions("firefox_extensions", node.get("id"))
        chrome_extensions = get_extensions("chrome_extensions", node.get("id"))
        if firefox_extensions is None:
            st.error("Error fetching firefox extensions!")
            return
        if chrome_extensions is None:
            st.error("Error fetching chrome extensions!")
            return
        total_extensions += firefox_extensions["totalItems"]
        total_extensions += chrome_extensions["totalItems"]

    with st.container(border=True):
        st.subheader("Statistics")
        col1, col2 = st.columns(2)
        col1.metric("**Nodes (Users)**", nodes["totalItems"])
        col2.metric("**Extensions**", total_extensions)

    with st.container(border=True):
        st.subheader("API Key")
        st.write("You need this for CLI")
        show = st.toggle("Show/hide API Key")
        if show:
            st.info(api_key)


def build_page():
    st.set_page_config(page_title="Dashboard")
    st.header("Dashboard")
    if st.sidebar.button("Logout"):
        LoginForm().logout()

    populate_page()


def main():
    if not LoginForm().is_logged_in():
        auth_form()
    else:
        build_page()


if __name__ == "__main__":
    main()
