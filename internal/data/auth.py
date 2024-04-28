import json

from pyrebase import pyrebase


def pb_auth():
    auth = pyrebase.initialize_app(
        json.load(open("./configs/firebase-pyrebase.json"))
    ).auth()
    return auth
