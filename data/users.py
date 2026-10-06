from config.settings import (
    STANDARD_USERNAME,
    STANDARD_PASSWORD
    )

STANDARD_USER = {
    "username": STANDARD_USERNAME,
    "password": STANDARD_PASSWORD
}

INVALID_USER = {
    "username": "Wrong_User",
    "password": "Wrong_password"
}

LOCKED_USER = {
    "username": "locked_out_user",
    "password":"STANDARD_PASSWORD"
}