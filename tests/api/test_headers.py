import pytest
from api.api_client import APIClient
from config.settings import API_URL

@pytest.mark.api
def test_bearer_token_header():
    client = APIClient(
        base_url=API_URL,
        token="test-token2"
        )
    authorization = client.session.headers.get("Authorization")
    print(f"\nToken is : {authorization}")
    assert authorization == "Bearer test-token2"

    client.session.close()
