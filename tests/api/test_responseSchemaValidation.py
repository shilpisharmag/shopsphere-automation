import pytest
from api.api_client import APIClient
from config.settings import API_URL
from data.schemas.post_schema import POST_SCHEMA 
from jsonschema import validate
from jsonschema.exceptions import ValidationError

@pytest.mark.api
def test_api_response_time(api_client):
    response = api_client.get("posts/1")

    assert response.status_code == 200
    '''
    response.elapsed is a timedelta recording the time 
    between sending the request and receiving the response headers. 
    .total_seconds() converts it to a float:
    '''
    responsetime = response.elapsed.total_seconds() # 
    print(f"Response time for get request is: {responsetime}")
    print(f"Round of time is: {responsetime:.3f}")

    assert responsetime < 3.0

@pytest.mark.api
def test_post_response_schema(api_client):
    response = api_client.get("posts/1")

    assert response.status_code ==200

    data = response.json()
    validate(instance=data,schema=POST_SCHEMA)
        