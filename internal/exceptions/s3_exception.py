
class S3CredentialsError(Exception):
    def __init__(self, message="S3 credentials are missing. "
                               "Please provide valid credentials."):
        self.message = message
        super().__init__(self.message)
