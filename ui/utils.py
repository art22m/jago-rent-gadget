import requests
import streamlit as st


def is_authenticated():
    return "user_info" in st.session_state


def raise_detailed_error(request_object):
    try:
        request_object.raise_for_status()
    except requests.exceptions.HTTPError as error:
        raise requests.exceptions.HTTPError(error, request_object.text)
