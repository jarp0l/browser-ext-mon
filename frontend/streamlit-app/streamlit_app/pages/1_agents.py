import streamlit as st

from streamlit_app.utils.auth_form import LoginForm, auth_form


def populate_page():
    st.write(
        "This page will soon be populated with a table of agents (CLI/Browser extensions) that admins can download."
    )


def build_page():
    st.set_page_config(page_title="Agents")
    st.header("Agents")
    st.subheader("Download agents from the list below")
    if st.sidebar.button("Logout"):
        LoginForm().logout()

    populate_page()


if not LoginForm().is_logged_in():
    auth_form()
else:
    build_page()
