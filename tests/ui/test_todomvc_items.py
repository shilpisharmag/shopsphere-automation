from playwright.sync_api import Page, expect

# Scenario: Add multiple todo items and verify each is displayed in the list.
def test_todomvc_add_items_and_verify_displayed(page: Page):
    todo_items = [
        "Learn Playwright",
        "Learn API testing",
        "Learn MCP",
    ]

    page.goto("https://demo.playwright.dev/todomvc")

    for item in todo_items:
        page.locator('.new-todo').fill(item)
        page.locator('.new-todo').press('Enter')

    expect(page.locator('.todo-list li')).to_have_count(len(todo_items))

    for item in todo_items:
        expect(page.locator('.todo-list')).to_contain_text(item)
