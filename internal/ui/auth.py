import json
import requests
import pyrebase
import streamlit as st

pb_auth = pyrebase.initialize_app(
    json.load(open("./configs/firebase-pyrebase.json"))
).auth()


def create_user_with_email_and_password(email, password):  # TODO: fixme
    request_ref = "https://www.googleapis.com/identitytoolkit/v3/relyingparty/signupNewUser?key={0}".format(
        st.secrets['FIREBASE_WEB_API_KEY'])
    headers = {"content-type": "application/json; charset=UTF-8"}
    data = json.dumps({"email": email, "password": password, "returnSecureToken": True})
    request_object = requests.post(request_ref, headers=headers, data=data)
    raise_detailed_error(request_object)
    return request_object.json()


def raise_detailed_error(request_object):
    try:
        request_object.raise_for_status()
    except requests.exceptions.HTTPError as error:
        raise requests.exceptions.HTTPError(error, request_object.text)


def sign_in(email: str, password: str) -> None:
    try:
        # Attempt to sign in with email and password
        id_token = pb_auth.sign_in_with_email_and_password(email, password)['idToken']

        # Get account information
        user_info = pb_auth.get_account_info(id_token)["users"][0]

        # If email is not verified, send verification email and do not sign in
        if not user_info["emailVerified"]:
            pb_auth.send_email_verification(id_token)
            st.session_state.auth_warning = 'Check your email to verify your account'

        # Save user info to session state and rerun
        else:
            st.session_state.user_info = user_info
            st.experimental_rerun()

    except requests.exceptions.HTTPError as error:
        error_message = json.loads(error.args[1])['error']['message']
        st.session_state.auth_warning = error_message

    except Exception as error:
        print(error)
        st.session_state.auth_warning = 'Error: Please try again later'


def create_account(email: str, password: str) -> None:
    try:
        id_token = create_user_with_email_and_password(email, password)['idToken']
        pb_auth.send_email_verification(id_token)
        st.session_state.auth_success = 'Check your inbox to verify your email'

    except requests.exceptions.HTTPError as error:
        error_message = json.loads(error.args[1])['error']['message']
        st.session_state.auth_warning = error_message

    except Exception as error:
        print(error)
        st.session_state.auth_warning = 'Error: Please try again later'


def reset_password(email: str) -> None:
    try:
        pb_auth.send_password_reset_email(email)
        st.session_state.auth_success = 'Password reset link sent to your email'

    except requests.exceptions.HTTPError as error:
        error_message = json.loads(error.args[1])['error']['message']
        st.session_state.auth_warning = error_message
    except Exception as e:
        st.session_state.auth_warning = str(e)


def sign_out() -> None:
    st.session_state.clear()
    st.session_state.auth_success = 'You have successfully signed out'


def delete_account(password: str) -> None:
    try:
        # Confirm email and password by signing in (and save id_token)
        id_token = pb_auth.sign_in_with_email_and_password(st.session_state.user_info['email'], password)['idToken']

        # Attempt to delete account
        pb_auth.delete_user_account(id_token)
        st.session_state.clear()
        st.session_state.auth_success = 'You have successfully deleted your account'

    except requests.exceptions.HTTPError as error:
        error_message = json.loads(error.args[1])['error']['message']
        st.session_state.auth_warning = error_message

    except Exception as error:
        print(error)
