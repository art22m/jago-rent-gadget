from unittest.mock import Mock

CREATE_USER_RESPONSE = "success"


def override_pb_auth():
    auth = Mock()
    auth.create_user_with_email_and_password.return_value = CREATE_USER_RESPONSE
    return auth