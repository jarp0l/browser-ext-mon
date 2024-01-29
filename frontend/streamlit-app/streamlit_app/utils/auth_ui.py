import streamlit as st

from streamlit_app.utils.auth import login, signup


def login_form():
    with st.form(key="login", clear_on_submit=True):
        st.subheader("Login")
        email = st.text_input(":blue[Email]", placeholder="Enter Your Email")
        password = st.text_input(
            ":blue[Password]", placeholder="Enter Your Password", type="password"
        )

        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn3:
            submitted = st.form_submit_button("Login")

        if submitted:
            res = login(email, password)
            if res != {}:
                st.session_state["token"] = res["token"]
                st.success("Login Successful")
                st.rerun()  # refresh page
            else:
                st.error("Login Failed")


def signup_page():
    with st.form(key="signup", clear_on_submit=True):
        st.subheader("Sign Up")
        email = st.text_input(":blue[Email]", placeholder="Enter Your Email")
        password = st.text_input(
            ":blue[Password]", placeholder="Enter Your Password", type="password"
        )
        passwordConfirm = st.text_input(
            ":blue[Confirm Password]",
            placeholder="Confirm Your Password",
            type="password",
        )

        btn1, bt2, btn3, btn4, btn5 = st.columns(5)

        with btn3:
            submitted = st.form_submit_button("Sign Up")

        if submitted:
            res = signup(email, password, passwordConfirm)
            if res != {}:
                st.success("Signup Successful")
                # st.rerun()  # refresh page
            else:
                st.error("Signup Failed")
