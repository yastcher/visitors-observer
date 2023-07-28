from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


pytest_plugins = [
    "tests.fixtures",
]
