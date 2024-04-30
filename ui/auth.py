import os

import pyrebase
import requests
import streamlit as st

import ui.utils as utils

fb_config = {
    "type": os.environ.get("TYPE"),
    "project_id": os.environ.get("PROJECTID"),
    "private_key_id": os.environ.get("PRIVATEKEYID"),
    "private_key": os.environ.get("PRIVATEKEY"),
    "client_email": os.environ.get("CLIENTEMAIL"),
    "client_id": os.environ.get("CLIENTID"),
    "token_uri": os.environ.get("TOKENURI"),
    "apiKey": os.environ.get("APIKEY"),
    "authDomain": os.environ.get("AUTHDOMAIN"),
    "projectId": os.environ.get("PROJECTID"),
    "databaseURL": "",
    "storageBucket": ""
}

pb_auth = pyrebase.initialize_app(fb_config).auth()


def create_user_with_email_and_password(email, username, password):
    request_ref = "http://0.0.0.0:8001/api/user"
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "name": username, "password": password})
    request_object = requests.post(request_ref, headers=headers,
                                   data=data, timeout=10)
    utils.raise_detailed_error(request_object)
    return request_object.json()


def signin_with_email_and_password(email, password):
    request_ref = "http://0.0.0.0:8001/api/user/signin"
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password})
    request_object = requests.get(request_ref, headers=headers,
                                  data=data, timeout=10)
    utils.raise_detailed_error(request_object)
    return request_object.json()


def sign_in(email: str, password: str) -> None:
    try:
        user = signin_with_email_and_password(email, password)
        st.session_state.user_info = user
        st.switch_page("pages/user_page.py")
        st.experimental_rerun()

    except requests.exceptions.HTTPError as error:
        st.session_state.auth_warning = json.loads(error.args[1])["detail"]

    except Exception as error:
        st.session_state.auth_warning = "Error: Please try again later" + str(
            error
        )


def create_account(email: str, username: str, password: str) -> None:
    try:
        user = create_user_with_email_and_password(email, username, password)
        st.session_state.user_info = user
        st.switch_page("pages/user_page.py")
        st.experimental_rerun()

    except requests.exceptions.HTTPError as error:
        st.session_state.auth_warning = json.loads(error.args[1])["detail"]

    except Exception as error:
        st.session_state.auth_warning = "Error: Please try again later" + str(
            error
        )


def reset_password(email: str) -> None:
    try:
        pb_auth.send_password_reset_email(email)
        st.session_state.auth_success = (
            "Password reset link sent to your email"
        )

    except requests.exceptions.HTTPError as error:
        error_message = json.loads(error.args[1])["error"]["message"]
        st.session_state.auth_warning = error_message
    except Exception as error:
        st.session_state.auth_warning = "Error: Please try again later" + str(
            error
        )


def sign_out() -> None:
    st.session_state.clear()
    st.session_state.auth_success = "You have successfully signed out"


def delete_account(password: str) -> None:
    try:
        id_token = pb_auth.sign_in_with_email_and_password(
            st.session_state.user_info["email"], password
        )["idToken"]

        pb_auth.delete_user_account(id_token)
        st.session_state.clear()
        st.session_state.auth_success = (
            "You have successfully deleted your account"
        )

    except requests.exceptions.HTTPError as error:
        error_message = json.loads(error.args[1])["error"]["message"]
        st.session_state.auth_warning = error_message

    except Exception as error:
        print(error)
