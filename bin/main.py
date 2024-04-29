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
        "type": os.environ.get("type"),
        "project_id": os.environ.get("projectId"),
        "private_key_id": os.environ.get("privateKeyId"),
        "private_key": os.environ.get("privateKey"),
        "client_email": os.environ.get("clientEmail"),
        "client_id": os.environ.get("clientId"),
        "token_uri": os.environ.get("tokenUri"),
        "apiKey": os.environ.get("apiKey"),
        "authDomain": os.environ.get("authDomain"),
        "projectId": os.environ.get("projectId"),
        "databaseURL": "",
        "storageBucket": ""
    }

    if not firebase_admin._apps:
        firebase_admin.initialize_app(credentials.Certificate(fb_config))
        pyrebase.initialize_app(fb_config).auth()

    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="127.0.0.1", port=8001)
