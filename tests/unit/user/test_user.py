def test_get_items(client):
    client.post("api/user")
    response = client.get("/api/item/")
    assert response.status_code == 200
