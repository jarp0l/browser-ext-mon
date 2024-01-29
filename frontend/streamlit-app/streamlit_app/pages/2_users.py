import streamlit as st

from streamlit_app.utils.auth import is_logged_in
from streamlit_app.utils.auth_ui import login_form


def build_page():
    st.set_page_config(page_title="Users")
    st.header("Users")

    st.write("List of users")


if not is_logged_in():
    login_form()
else:
    build_page()
