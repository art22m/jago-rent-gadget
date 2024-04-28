import json
import uuid

import internal.ui.utils as utils
import requests
import streamlit as st
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
            "owner_id": 1,  # TODO(art22m): change to real
        }
    )
    headers = {
        "content-type": "application/json; charset=UTF-8",
        # "Authorization": st.session_state.user_token,
    }

    request_object = requests.post(request_ref, headers=headers, data=data)
    try:
        utils.raise_detailed_error(request_object)
        st.success("Added")
        # st.experimental_rerun()
    except requests.exceptions.HTTPError as error:
        # error_message = json.loads(error.args[1])["detail"]
        st.session_state.create_warning = str(error)
    except Exception as error:
        print(error)
        st.session_state.create_warning = "Error: Please try again later"
