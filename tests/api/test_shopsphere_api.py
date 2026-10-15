import requests

BASE_URL =  "http://127.0.0.1:5000"

def test_health_endpoint(shopsphere_api_client):
    response = shopsphere_api_client.get("health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_all_products(shopsphere_api_client):
    response = shopsphere_api_client.get("products")
    assert response.status_code == 200
    products = response.json()
    assert len(products) == 2
    assert products[0]["name"] == "Laptop"
    assert products[1]["name"] == "Headphones"


def test_get_product__byID(shopsphere_api_client):
    response = shopsphere_api_client.get("product/1")
    assert response.status_code == 200
    products = response.json()
    assert products["name"] == "Laptop"
    assert products["price"] == 75000
    assert products["stock"] == 10

def test_product_notfound(shopsphere_api_client):
    response = shopsphere_api_client.get("product/4999")
    assert response.status_code == 404
    assert response.json()["error"] =="Product not found"

def test_products_have_valid_data(shopsphere_api_client):
    response = shopsphere_api_client.get("products")
    assert response.status_code == 200
    products = response.json()
    for product in products:
        assert isinstance(product["id"],int)
        assert isinstance(product["name"],str)
        assert product["name"].strip()!= ""
        assert isinstance(product["price"],(int, float))
        assert product["price"]>= 0
        assert isinstance(product["stock"],int)
        assert product["stock"] >= 0


