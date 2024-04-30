import os

import firebase_admin
import pyrebase
import uvicorn
from fastapi import FastAPI
from firebase_admin import credentials

from internal.data.database import Base, engine
from internal.item.router import router as item_router
from internal.user.router import router as user_router


def create_app() -> FastAPI:
    app = FastAPI()
    app.include_router(item_router, prefix="/api")
    app.include_router(user_router, prefix="/api")

    Base.metadata.create_all(bind=engine)

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

    if not firebase_admin._apps:
        firebase_admin.initialize_app(credentials.Certificate(fb_config))
        pyrebase.initialize_app(fb_config).auth()

    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8001)
