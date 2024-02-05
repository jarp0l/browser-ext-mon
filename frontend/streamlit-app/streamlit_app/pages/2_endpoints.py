import streamlit as st

from streamlit_app.utils.auth_form import LoginForm, auth_form


def populate_page():
    st.write("Hello World!")


def build_page():
    st.set_page_config(page_title="Endpoints")
    st.header("Endpoints")
    st.subheader("List of endpoints")
    if st.sidebar.button("Logout"):
        LoginForm().logout()

    populate_page()


if not LoginForm().is_logged_in():
    auth_form()
else:
    build_page()
