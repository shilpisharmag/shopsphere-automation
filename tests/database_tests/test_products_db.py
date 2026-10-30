from database.db import get_connection
import sqlite3, pytest

def test_products_table_contains_expected_products():
     """Verify that expected products exist in the database."""
     with get_connection() as connection:
          rows = connection.execute("SELECT id, name, price, stock FROM products ORDER BY id").fetchall()

          products = [dict(row) for row in rows]
          assert len(products) > 0
          assert products[0]['id'] == 1

def test_product_price_and_stock_are_valid():
    """Verify product prices and stock quantities are valid."""
    with get_connection() as connection:
        rows = connection.execute(
            "SELECT price, stock FROM products"
        ).fetchall()

    assert rows, "Expected at least one product in the database"

    for row in rows:
        assert row["price"] >= 0
        assert row["stock"] >= 0

def create_test_database(tmp_path):
    """Create an isolated database for constraint testing."""
    db_path = tmp_path / "test_shopsphere.db"

    connection = sqlite3.connect(db_path)

    connection.execute("""
        CREATE TABLE products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            price REAL NOT NULL CHECK (price >= 0),
            stock INTEGER NOT NULL CHECK (stock >= 0)
        )
    """)

    connection.commit()
    return connection


def test_database_rejects_duplicate_product_id(tmp_path):
    """Verify that duplicate product IDs are rejected."""
    with create_test_database(tmp_path) as connection:
        connection.execute(
            "INSERT INTO products VALUES (?, ?, ?, ?)",
            (1, "Laptop", 75000, 10),
        )

        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO products VALUES (?, ?, ?, ?)",
                (1, "Monitor", 15000, 5),
            )


def test_database_rejects_negative_price(tmp_path):
    """Verify that negative product prices are rejected."""
    with create_test_database(tmp_path) as connection:
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO products VALUES (?, ?, ?, ?)",
                (3, "Keyboard", -500, 10),
            )


def test_database_rejects_negative_stock(tmp_path):
    """Verify that negative stock quantities are rejected."""
    with create_test_database(tmp_path) as connection:
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO products VALUES (?, ?, ?, ?)",
                (4, "Mouse", 800, -2),
            )


def test_database_rejects_null_product_name(tmp_path):
    """Verify that a product cannot have a NULL name."""
    with create_test_database(tmp_path) as connection:
        with pytest.raises(sqlite3.IntegrityError):
            connection.execute(
                "INSERT INTO products VALUES (?, ?, ?, ?)",
                (5, None, 500, 10),
            )