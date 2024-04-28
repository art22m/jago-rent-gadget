from tests.e2e.conftest import generate_random_email


def test_create_item__happy_path(client):
    email = generate_random_email()
    client_id = client.post(
        "api/user",
        json={"email": email, "password": "password", "name": "name"}
    ).json()["id"]

    create_response = client.post(
        "api/item",
        json={
            "title": "title",
            "description": "description",
            "s3_url": "http://s3",
            "price": 150,
            "owner_id": client_id
        }
    )
    item_id = create_response.json()["id"]
    assert create_response.json() == {
        "id": item_id,
        "title": "title",
        "description": "description",
        "s3_url": "http://s3",
        "price": 150,
        "owner_id": client_id
    }
    assert create_response.status_code == 200

    get_response_item = client.get(
        f"api/item/{item_id}"
    )
    assert get_response_item.json() == {'description': 'description',
                                        'id': item_id,
                                        'owner_id': 1,
                                        'price': 150,
                                        's3_url': 'http://s3',
                                        'title': 'title'}
    assert get_response_item.status_code == 200

    get_response_client = client.get(
        "api/user"
    )
    assert get_response_client.json() == [{'email': email,
                                           'id': 1,
                                           'items': [{'description': 'description',
                                                      'id': 1,
                                                      'owner_id': client_id,
                                                      'price': 150,
                                                      's3_url': 'http://s3',
                                                      'title': 'title'}],
                                           'name': 'name'}]
    assert get_response_client.status_code == 200
