def test_status(client):
    response = client.get("/status")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "OK"
    assert "timestamp" in data


def test_root(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["status"] == "OK"
