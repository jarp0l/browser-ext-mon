import streamlit as st
import pandas as pd

from streamlit_app.utils.auth_form import LoginForm, auth_form
# from streamlit_app.utils.apis import make_get_request
# from streamlit_app.dashboard import populate_node_page
from streamlit_app.utils.apis import get_nodes


def populate_page():
    
    org_id_here="72b53p7ai8s9wdm"
    
    nodes = get_nodes(org_id_here)
    if nodes is None:
        st.error("Error fetching nodes!")
        return
    if  nodes['totalItems']:
        df = pd.DataFrame(nodes["items"])
        st.data_editor(df)
    else:
        st.error("total items in node is zero")
    


def build_page():
    st.set_page_config(page_title="Nodes")
    st.header("Nodes")
    st.subheader("List of nodes")
    if st.sidebar.button("Logout"):
        LoginForm().logout()
    populate_page()


if not LoginForm().is_logged_in():
    auth_form()
else:
    build_page()
