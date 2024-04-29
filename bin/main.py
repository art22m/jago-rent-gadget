import json

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

    if not firebase_admin._apps:
        cred = credentials.Certificate("./configs/firebase-adminsdk.json")
        pyrebase.initialize_app(
            json.load(open("./configs/firebase-pyrebase.json")),
        ).auth()
        firebase_admin.initialize_app(cred)

    return app


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8001)
