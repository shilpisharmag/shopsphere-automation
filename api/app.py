from flask import Flask,jsonify
from flask import send_from_directory
from pathlib import Path
import os

app = Flask(__name__)

products = [
    {
        "id" : 1,
        "name" : "Laptop",
        "price" : 75000,
        "stock" : 10,

    },
    {
        "id" : 2,
        "name" : "Headphones",
        "price" : 2500,
        "stock" : 20
    }
]

@app.get("/")
def home():
    return send_from_directory(
        Path(__file__).resolve().parent.parent /
        "ui",
        "shopsphere.html"
    )

@app.get("/health")
def health():
    return jsonify({"status" : "ok"}), 200


@app.get("/products")
def get_products():
    return jsonify(products), 200

@app.get("/product/<int:product_id>")
def getproduct(product_id):
    for product in products:
        if product["id"] == product_id:
            return jsonify(product), 200
    return jsonify({"error": "Product not found"}), 404

@app.errorhandler(404)
def handle_not_found(error):
    return jsonify({"error": "Not Found"}), 404


if __name__ == "__main__":
    host = os.getenv("FLASK_HOST","127.0.0.1")
    app.run(host = host, port=5000, debug=False)
