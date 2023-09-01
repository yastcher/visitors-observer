import pytest


@pytest.fixture()
def healthcheck():
    return "/status"
