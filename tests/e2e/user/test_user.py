from tests.e2e.fixtures import generate_random_email


def test_register_user__happy_path(client):
    email = generate_random_email()
    create_response = client.post(
        "api/user",
        json={"email": email, "password": "password", "name": "name"}
    )
    id = create_response.json()["id"]
    assert create_response.json() == {'email': email, 'id': id, 'name': 'name'}
    assert create_response.status_code == 200

    get_response = client.get(
        f"api/user/{id}"
    )
    assert get_response.json() == {'email': email, 'id': id, 'items': [], 'name': 'name'}
    assert get_response.status_code == 200

    new_email = generate_random_email()
    update_response = client.put(
        "api/user",
        json={"id": id, "email": new_email, "name": "new_name"}
    )
    assert update_response.json() == {'email': new_email, 'id': id, 'items': [], 'name': 'new_name'}
    assert update_response.status_code == 200
