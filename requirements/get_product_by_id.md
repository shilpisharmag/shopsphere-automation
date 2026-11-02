
# Requirement: retrieve product with id


## EndPoint
GET /product/{product_id}

## Description
The API should retrieve a product using its unique Given product id from the SHOPSPHERE SQLite database.


## Acceptance Criteria

1. When a valid exisiting  product ID is provided:
 - Return HTTP status code  200.
 - Return the product details as JSON.
 - The response must contain id, name, price and stock.

2. When a product ID does not exist:
 - Return HTTP status code 404.
 - Return the error message "Product not found".

3. When the product ID is not integer:
 - Return HTTP status code 404.
 - Return the error message "Product not found".

4. The API must not return product different from the requested ID.
