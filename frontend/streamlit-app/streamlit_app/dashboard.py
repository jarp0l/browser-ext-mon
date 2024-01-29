import streamlit as st

from streamlit_app.utils.auth import is_logged_in
from streamlit_app.utils.auth_ui import login_form


def build_page():
    st.set_page_config(page_title="Dashboard")
    st.header("Dashboard")

    st.write("Hello World!")


def main():
    if not is_logged_in():
        login_form()
    else:
        build_page()


if __name__ == "__main__":
    main()
    # asyncio.run(main())
