import pytest

@pytest.fixture
def test_user():
    return {
        "username": "testuser",
        "password": "Test@123"
    }