import logging
import os
import time

import httpx
import streamlit as st

from streamlit_app.utils.init_redis import r

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8090/api")
TOKEN_EXPIRY = os.getenv("TOKEN_EXPIRY", 1209600)

logging.basicConfig(level=logging.ERROR)


class AuthForm:
    def __init__(self, form_key, form_submit_label, form_submit_action):
        self.form_key = form_key
        self.form_submit_label = form_submit_label
        self.form_submit_action = form_submit_action

    def display_form(self):
        with st.form(key=self.form_key, clear_on_submit=True):
            self.render_form_content()

            _, _, btn3, _, _ = st.columns(5)

            with btn3:
                submitted = st.form_submit_button(self.form_submit_label)

            if submitted:
                self.handle_form_submit()

    def render_form_content(self):
        raise NotImplementedError("Subclasses must implement this method")

    def handle_form_submit(self):
        raise NotImplementedError("Subclasses must implement this method")

    def make_request(self, method, endpoint, data):
        try:
            res = httpx.request(method, f"{API_BASE_URL}{endpoint}", json=data)
            if res.status_code == 200:
                return res.json()
            elif res.status_code in [400, 403]:
                logging.error(res.json())
                return {}
        except Exception as e:
            logging.error(e)
            return {}


class LoginForm(AuthForm):
    def __init__(self):
        super().__init__("login", "Login", self.handle_form_submit)

    def render_form_content(self):
        st.subheader("Login")
        self.email = st.text_input(":blue[Email]", placeholder="Enter your email")
        self.password = st.text_input(
            ":blue[Password]", placeholder="Enter your password", type="password"
        )

    def handle_form_submit(self):
        with st.spinner("Logging in..."):
            res = self.make_request(
                "post",
                "/collections/users/auth-with-password",
                {"identity": self.email, "password": self.password},
            )
            if res != {}:
                self.set_logged_in(res["token"])
                st.success("Login Successful! 😃")
                time.sleep(0.5)
                st.rerun()
            else:
                st.error("Login Failed! 😞")

    def is_logged_in(self):
        if "bem-token" in st.session_state:
            return True

        r_bem_token = r.get("bem-token")
        if r_bem_token is None:
            return False
        else:
            st.session_state["bem-token"] = r_bem_token
            return True

    def set_logged_in(self, token: str):
        st.session_state["bem-token"] = token
        r.set("bem-token", token, ex=1209600)

    def logout(self):
        r.delete("bem-token")
        del st.session_state["bem-token"]
        st.rerun()


class SignupForm(AuthForm):
    def __init__(self):
        super().__init__("signup", "Sign Up", self.handle_form_submit)

    def render_form_content(self):
        st.subheader("Sign Up")
        self.email = st.text_input(":blue[Email]", placeholder="Enter your email")
        self.password = st.text_input(
            ":blue[Password]", placeholder="Enter your password", type="password"
        )
        self.password_confirm = st.text_input(
            ":blue[Confirm Password]",
            placeholder="Confirm your password",
            type="password",
        )

        st.divider()
        st.markdown("**Create organization**")

        self.org_name = st.text_input(
            ":blue[Organization Name]", placeholder="Enter your organization name"
        )
        self.org_slug = st.text_input(
            ":blue[Organization Slug]",
            placeholder="Enter short name for your organization",
        )

    def handle_form_submit(self):
        with st.spinner("Signing up..."):
            res1 = self.make_request(
                "post",
                "/collections/users/records",
                {
                    "email": self.email,
                    "password": self.password,
                    "passwordConfirm": self.password_confirm,
                },
            )
            if res1 != {}:
                st.success("Signup successful!")
            else:
                st.error("Signup Failed! 😞")
                return

        with st.spinner("Creating organization..."):
            res2 = self.make_request(
                "post",
                "/collections/organizations/records",
                {
                    "orgSlug": self.org_slug,
                    "orgName": self.org_name,
                    # "email": self.email,
                },
            )
            if res2 != {}:
                st.success("Organization created!")
            else:
                st.error("Organization could not be created! 😞")
                return

        st.success("Signed you up and created your organization. You can login now! 😃")
        time.sleep(1)


def auth_form():
    login_form = LoginForm()
    signup_form = SignupForm()

    login_form.display_form()

    st.divider()
    st.write("Don't have an account? Sign up :point_down:")
    st.divider()

    signup_form.display_form()


# login_form = LoginForm()
