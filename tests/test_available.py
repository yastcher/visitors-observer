from tests.conftest import client


def test_status(healthcheck):
    with client:
        response = client.get(healthcheck)
        assert response.status_code == 200
        assert response.json().get("status") == "OK"
