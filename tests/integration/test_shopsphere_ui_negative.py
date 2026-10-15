from playwright.sync_api import Page
import pytest
from config.settings import SHOPSPHERE_API_URL


def test_ui_shows_error_when_api_fails(page:Page):
    #intercept the product API request and simulate a server error
    page.route(
        "**/products",
        lambda route: route.fulfill(
            status=500,
            content_type="application/json",
            body='{"error":"Internal Server error"}',
        ),
    )
    page.goto(SHOPSPHERE_API_URL)

    # Verify that the ui displays an error instead of staying on loading
    page.locator("#products").wait_for()

    assert page.locator("#products").inner_text() == ("Failed to load Products: HTTP error: 500")