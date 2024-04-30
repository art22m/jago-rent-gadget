import os

from pyrebase import pyrebase

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


def pb_auth():
    return pyrebase.initialize_app(fb_config).auth()
