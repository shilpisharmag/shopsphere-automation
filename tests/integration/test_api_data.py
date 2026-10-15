import pytest

@pytest.mark.intergration
def test_validated_post_data(validated_post):
    assert validated_post["id"] == 1
    assert validated_post["userId"] == 1

    print("Post tilte:", validated_post["title"])


@pytest.mark.integration
@pytest.mark.parametrize("post_id",
                         [1,2,3])
def test_post_details(api_client,post_id):
    response = api_client.get(f"posts/{post_id}")

    assert response.status_code == 200
    post =  response.json()
    assert post["id"] == post_id
    assert post["userId"] == 1

@pytest.mark.integration
@pytest.mark.parametrize("validated_multi_post",
                         [1,2,3],
                         indirect=True)
def test_post_multifixture(validated_multi_post):
    assert validated_multi_post["id"] in [1, 2, 3]
  

@pytest.mark.api
def test_api_data_fixture_request(validated_post,api_client):
    userid = validated_post["id"]
    response = api_client.get(f"users/{userid}")
    response.status_code == 200
    data = response.json() 
    print(f"\n data: {data}")