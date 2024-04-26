import json

import pyrebase
import firebase_admin
from firebase_admin import credentials

from internal.user.auth import Auther


def main():
    # Тут надо бы все инициализировать и прокидывать в классы, и классы в классы, aka DI
    # fb_config = credentials.Certificate("path/to/service.json")
    pb_auth = pyrebase.initialize_app(json.load(open('../configs/firebase-pyrebase.json'))).auth()
    cred = credentials.Certificate("../configs/firebase-adminsdk.json")
    firebase_admin.initialize_app(cred)

    # auth = Auther(pb_auth)
    # user = auth.register("test@mail.ru", "123456")
    # user = auth.sign_in("test@mail.ru", "123456")
    # print(user)
    #
    # auth.verify(user["idToken"])
    #
    # user = auth.refresh_token(user)
    # print(user)
    #
    # auth.verify(user["idToken"])


if __name__ == "__main__":
    main()
