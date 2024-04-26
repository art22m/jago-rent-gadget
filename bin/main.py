import json

import uvicorn
import pyrebase
import firebase_admin
from fastapi import FastAPI
from firebase_admin import credentials

from internal.user.auth import Auther
from internal.data.database import engine, Base
from internal.item.router import router as item_router
from internal.user.router import router as user_router


def main():
    app = FastAPI()
    Base.metadata.create_all(bind=engine)
    app.include_router(item_router, prefix="/api")
    app.include_router(user_router, prefix="/api")

    # Тут надо бы все инициализировать и прокидывать в классы, и классы в классы, aka DI
    # fb_config = credentials.Certificate("path/to/service.json")
    pb_auth = pyrebase.initialize_app(
        json.load(open("./configs/firebase-pyrebase.json"))
    ).auth()
    cred = credentials.Certificate("./configs/firebase-adminsdk.json")
    firebase_admin.initialize_app(cred)

    auth = Auther(pb_auth)
    # user = auth.register("test@mail.ru", "123456")
    user = auth.sign_in("test@mail.ru", "123456")
    print(user)
    #
    # auth.verify(user["idToken"])
    #
    # print(auth.verify(user["idToken"]))
    #
    # user = auth.refresh_token(user)
    # print(auth.verify(user["idToken"]))

    uvicorn.run(app, host='0.0.0.0', port=8001)


if __name__ == "__main__":
    main()
