# use pydantic to check email and password
import httpx
import streamlit as st

API_BASE_URL = "http://localhost:8090/api"


def login(email: str, password: str):
    try:
        res = httpx.post(
            f"{API_BASE_URL}/collections/users/auth-with-password",
            json={"identity": email, "password": password},
        )
        if res.status_code == 200:
            return res.json()
        elif res.status_code == 400:
            print("Error: ", res.json())
            return {}
    except Exception as e:
        print("Error: ", e)
        return {}


def signup(email: str, password: str, passwordConfirm: str):
    try:
        res = httpx.post(
            f"{API_BASE_URL}/collections/users/records",
            json={
                "email": email,
                "password": password,
                "passwordConfirm": passwordConfirm,
            },
        )
        return res.json()
    except Exception as e:
        print("Error: ", e)
        return {}


def is_logged_in():
    try:
        return bool(st.session_state["token"])
    except Exception as e:
        print("Error: ", e)
        return False
