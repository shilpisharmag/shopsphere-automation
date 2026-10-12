import pytest

@pytest.mark.api
def test_get_single_post(api_client):
    response = api_client.get("posts/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    assert data["title"] != ""

@pytest.mark.api
def test_get_all_Posts(api_client):
    response = api_client.get("posts")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data,list)

    assert len(data) > 0

    assert data[1]["id"] == 2
    assert data[1]["userId"] == 1


@pytest.mark.api
def test_get_filter_post_by_user(api_client):
    response = api_client.get("posts",
                              params={"userId": 1})

    assert response.status_code == 200
    data = response.json()

    assert len(data) > 0

    # assert all(post["userId"] == 1 for post in data)

    for post in data:
        assert post["userId"] == 1

# checked negative case too
@pytest.mark.api
def test_get_nonexistent_post(api_client):
    response = api_client.get("posts/99999")
    assert response.status_code == 404

@pytest.mark.api
def test_create_post_request(api_client):
    payload = {
        "title":"foo",
        "body":"bar",
        "userId":1
    }
    headers= {
        "content-type" : "application/json; chartset = UTF-8"
    }
    response = api_client.post("posts",payload)
    assert response.status_code == 201

    data = response.json()
    
    print(data)
    assert data["title"] == payload["title"]
    assert data["userId"] == payload["userId"]
    assert isinstance(data, dict)
    assert isinstance(data['id'], int)


@pytest.mark.api
def test_create_post_request_withoutTitle(api_client):
    payload = {
        "body":"bar",
        "userId":1
    }
    headers= {
        "content-type" : "application/json; chartset = UTF-8"
    }
    response = api_client.post("posts",payload)
    print(response.status_code)

    data = response.json()


@pytest.mark.api
def test_create_post_request_EmptyBody(api_client):
    payload = {
        
    }

    response = api_client.post("posts",payload)
    print(response.status_code) # it should return 400 error    
 
    data = response.json()


@pytest.mark.api
def test_create_put_request(api_client):
    payload = {
        "id" : 1,
        "title":"updating api",
        "body":"updated context",
        "userId":1
    }

    response = api_client.put("posts/1",payload)
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "updating api"
    assert data["id"] == 1

@pytest.mark.api
@pytest.mark.parametrize("post_id",
                         [1,2,3,4,5])
def test_get_multiple_posts(api_client,post_id):
    response = api_client.get(f"posts/{post_id}")
    assert response.status_code == 200
    data = response.json()

@pytest.mark.api
def test_api_chaining_post_to_user(api_client):
    post_response = api_client.get("posts/1")
    assert post_response.status_code == 200
    post_data = post_response.json()
    userid = post_data["userId"]

    user_response = api_client.get(f"users/{userid}")
    assert user_response.status_code == 200
    data = user_response.json()
    print(data)
    assert data["id"] == userid

    print(f"\nPost {post_data['id']} belongs to" f"{data['name']}")

@pytest.mark.api
def test_get_comment_by_postid_id(api_client):
    response = api_client.get("comments",params = {
        "userId" : 1,
        "id" : 1
    })
    assert response.status_code == 200
    data = response.json()
    print(data)
    assert data[0]["postId"] == 1


@pytest.mark.api
@pytest.mark.parametrize("postid",[999999,1000000])
def test_datadriven_for_get_postbyId(api_client,postid):
    response = api_client.get(f"posts/{postid}")
    data = response.json()
    assert response.status_code == 404
    print(response.headers)
    print(f"\n{data}")

pytest.mark.api
def test_get_user_by_postcall_userid(api_client):
    response = api_client.get("posts/1")
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["userId"] == 1
    userid = data["userId"]

    useres = api_client.get(f"users/{userid}")
    useres.status_code == 200
    useresData = useres.json()
    print(useresData)
    assert data["userId"] == useresData["id"]


    


    

