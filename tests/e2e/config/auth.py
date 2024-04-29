from unittest.mock import Mock

CREATE_USER_RESPONSE = "success"


def override_pb_auth():
    auth = Mock()
    auth.create_user_with_email_and_password.return_value = {
        "sessionId": "as314v"
    }
    auth.verify_id_token.return_value = "success"
    return auth
