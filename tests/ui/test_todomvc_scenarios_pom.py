from playwright.sync_api import expect

from pages.todomvc_pom_page import TodoMvcPage

# Scenario: Add multiple todos and verify each item is displayed in the list.
def test_add_multiple_todos_and_verify_displayed(page):
    todo_items = ['Learn Playwright', 'Learn API testing', 'Learn MCP']
    todo_page = TodoMvcPage(page)

    todo_page.open()
    todo_page.add_todos(todo_items)

    expect(todo_page.todo_items).to_have_count(len(todo_items))
    assert todo_page.get_todo_texts() == todo_items

    for item in todo_items:
        expect(page.locator('.todo-list')).to_contain_text(item)

# Scenario: Edit an existing todo item and verify the updated value is saved.
def test_edit_todo_item(page):
    todo_page = TodoMvcPage(page)
    todo_page.open()
    todo_page.add_todo('Learn Playwright')

    todo_page.edit_todo('Learn Playwright', 'Learn Playwright Advanced')

    expect(page.locator('.todo-list')).to_contain_text('Learn Playwright Advanced')
    expect(page.locator('.todo-list')).not_to_contain_text('Learn Playwright')

# Scenario: Complete a todo and verify it appears under the Completed filter.
def test_complete_todo_and_filter_completed(page):
    todo_items = ['Learn Playwright', 'Learn API testing', 'Learn MCP']
    todo_page = TodoMvcPage(page)

    todo_page.open()
    todo_page.add_todos(todo_items)
    todo_page.complete_todo('Learn API testing')
    todo_page.filter_by('Completed')

    expect(todo_page.todo_items).to_have_count(1)
    expect(page.locator('.todo-list')).to_contain_text('Learn API testing')

# Scenario: Clear completed todos and keep only active ones in the list.
def test_clear_completed_todos(page):
    todo_items = ['Learn Playwright', 'Learn API testing', 'Learn MCP']
    todo_page = TodoMvcPage(page)

    todo_page.open()
    todo_page.add_todos(todo_items)
    todo_page.complete_todo('Learn Playwright')
    todo_page.clear_completed()

    assert todo_page.get_todo_texts() == ['Learn API testing', 'Learn MCP']
    expect(page.locator('.todo-list')).not_to_contain_text('Learn Playwright')

# Scenario: Validate that a blank or whitespace-only todo is not added.
def test_empty_todo_is_not_added(page):
    todo_page = TodoMvcPage(page)

    todo_page.open()
    todo_page.new_todo_input.fill('   ')
    todo_page.new_todo_input.press('Enter')

    expect(todo_page.todo_items).to_have_count(0)
