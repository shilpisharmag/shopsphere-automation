from playwright.sync_api import expect

from pages.todomvc_page import TodoMvcPage

 # Scenario: Add todo items using the page object model and verify they are displayed.
def test_todomvc_add_items_via_pom(page):
    todo_items = [
        'Learn Playwright',
        'Learn API testing',
        'Learn MCP',
    ]

    todo_page = TodoMvcPage(page)
    todo_page.open()
    todo_page.add_todos(todo_items)

    expect(todo_page.todo_items).to_have_count(len(todo_items))

    for item in todo_items:
        expect(page.locator('.todo-list')).to_contain_text(item)
