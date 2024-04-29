import json
import uuid

import requests
import streamlit as st

import internal.ui.utils as utils
from internal.data.s3storage import Storage

creds = json.load(open("./configs/yandex-s3-creds.json"))
storage = Storage(
    endpoint_url=creds["endpoint"],
    bucket=creds["bucket"],
    access_key=creds["accessKey"],
    secret=creds["secret"],
)


def create_item(title, price, description, image):
    image_id = str(uuid.uuid4())
    try:
        storage.save_image(image_id, image)
    except Exception as e:
        st.error("Error", e)
        return

    request_ref = "http://0.0.0.0:8001/api/item"
    data = json.dumps(
        {
            "title": title,
            "description": description,
            "s3_url": image_id,
            "price": price,
            "owner_id": st.session_state.user_info["id"],
        }
    )
    headers = {
        "content-type": "application/json; charset=UTF-8",
        "Authorization": st.session_state.user_info["idToken"],
    }

    request_object = requests.post(request_ref, headers=headers, data=data, timeout=10)
    try:
        utils.raise_detailed_error(request_object)
        st.session_state.create_success = "Advertisement successfully created!"
    except requests.exceptions.HTTPError as error:
        st.session_state.create_warning = str(
            json.loads(error.args[1])["detail"]
        )
    except Exception as error:
        st.session_state.create_warning = (
            "Error: Please try again later " + str(error)
        )


def send_image(image):
    image_id = str(uuid.uuid4())
    storage.save_image(image_id, image)
    print(image_id)


def get_image_full_url(item_id):
    full_url = storage.get_image(item_id)
    return full_url


def get_user_info_by_id(user_id):
    request_ref = f"http://0.0.0.0:8001/api/user/{user_id}"
    return get_request_by_url(request_ref)


def get_user_id_by_email(email):
    request_ref = f"http://0.0.0.0:8001/api/user/by-email/{email}"
    return get_request_by_url(request_ref)


def get_items():
    request_ref = "http://0.0.0.0:8001/api/item/"
    return get_request_by_url(request_ref)


def get_request_by_url(url):
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException:
        return None


def delete_item(item_id):
    request_ref = f"http://0.0.0.0:8001/api/item/{item_id}"
    headers = {
        "content-type": "application/json; charset=UTF-8",
        "Authorization": st.session_state.user_info["idToken"],
    }
    try:
        response = requests.delete(request_ref, headers=headers, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            return None
    except requests.exceptions.RequestException:
        return None
