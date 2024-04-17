import boto3


class Storage:

    def __init__(self, service_name: str, endpoint_url: str, access_key: str, secret: str, bucket: str):
        assert access_key is not None
        assert secret is not None

        session = boto3.session.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret,
        )

        self.client = session.client(service_name=service_name, endpoint_url=endpoint_url)
        self.bucket = bucket

    def save_image(self, item_id, data):
        key = create_key(item_id)
        self.client.put_object(
            Bucket=self.bucket,
            Key=key,
            Body=data,
        )

    def get_image(self, item_id):
        key = create_key(item_id)
        data = self.client.get_object(Bucket=self.bucket, Key=key)["Body"].read()
        return data


def create_key(key):
    return f"images/{key}"

# if __name__ == "__main__":
#     d = "123"
#     access_key = ""
#     secret = ""
#
#     s3 = S3Storage("s3", "https://storage.yandexcloud.net", access_key, secret, "rent-gadget")
#     print(s3.get_image(""))
