import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv(
    "BASE_URL",
    "https://www.saucedemo.com/"
)

ENV = os.getenv("ENV","qa")

STANDARD_USERNAME = os.getenv("STANDARD_USERNAME","standard_user")
STANDARD_PASSWORD = os.getenv("STANDARD_PASSWORD","secret_sauce")