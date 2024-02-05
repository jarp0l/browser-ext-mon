import streamlit as st

from streamlit_app.utils.auth_form import LoginForm, auth_form


def build_page():
    st.set_page_config(page_title="Dashboard")
    st.header("Dashboard")
    if st.sidebar.button("Logout"):
        LoginForm().logout()

    st.write("Hello World!")


def main():
    if not LoginForm().is_logged_in():
        auth_form()
    else:
        build_page()


if __name__ == "__main__":
    main()
