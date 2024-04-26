import pyrebase
from firebase_admin import auth


# {'kind':
# 'idToken':
# 'email':
# 'refreshToken':


class Auther:
    def __init__(self, pbauth):
        # firebase = pyrebase.initialize_app("23")  # TODO: Remove
        self._auth = pbauth

    def register(self, email: str, password: str):
        print("Registering user ", email)
        user = self._auth.create_user_with_email_and_password(
            email=email, password=password
        )
        return user

    def sign_in(self, email: str, password: str):
        print("Login user ", email)
        user = self._auth.sign_in_with_email_and_password(
            email=email, password=password
        )
        return user

    # FIXME(art22m)
    def refresh_token(self, user):
        refreshed_user = self._auth.refresh(user["refreshToken"])
        return refreshed_user
