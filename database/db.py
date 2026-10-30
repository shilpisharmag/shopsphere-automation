import sqlite3
from pathlib import Path
DB_PATH = Path(__file__).resolve().parent / "shopsphere.db"

def get_connection(): # gives our test a reusable database connection 
    """
    Create a connection to the Shopsphere SQLite database."""
    connection = sqlite3.connect(DB_PATH) # provides database connectivity.DB_Path ensure database is stored at predictable location
    connection.row_factory = sqlite3.Row # let us access query results through column name
    return connection

def create_products_table():
    """
    create the table if it doesnot exist"""

    with get_connection() as connection:
        connection.execute("""

        CREATE TABLE  IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        price REAL NOT NULL CHECK (price >= 0),
        stock INTEGER NOT NULL CHECK (stock >= 0)
        )

        """)


def insert_products(products):
    """Create the products table if it does not exist."""
    "Insert products into the database without  creating duplicate."

    with get_connection() as connection:
        connection.executemany(
            """
            INSERT OR IGNORE INTO products (id, name, price, stock)
            VALUES (:id, :name, :price, :stock)""",
            products
        )

def get_all_products():
    """
    Retrieve all products fromt he database."""
    with get_connection() as connection:
        rows = connection.execute("SELECT id, name, price, stock FROM products ORDER BY id").fetchall()
        return [dict(row) for row in rows]

def get_product_by_id(product_id):
    """
    Retrieve its single product by its ID ."""

    with get_connection() as connection:
        row = connection.execute("SELECT id, name, price, stock FROM products WHERE id = ?",(product_id,)).fetchone()
        return dict(row) if row else None

