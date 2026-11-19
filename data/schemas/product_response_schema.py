PRODUCT_RESPONSE_SCHEMA = {
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "name": {"type": "string"},
        "price": {"type": "number"},
        "stock": {"type": "integer"}
    },
    "required": ["id", "name", "price", "stock"],
    "additionalProperties": False
}