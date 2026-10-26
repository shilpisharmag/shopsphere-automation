PRODUCT_SCEHMA = {
    "type": "object",
    "properties" : {
        "id": {"type" : "integer"},
        "name": {"type": "string"},
        "price": {"type": "integer"},
        "stock": {"type": "integer"}
    },
    "required": ["id", "name", "price", "stock"],
    "additionalProperties": False
}