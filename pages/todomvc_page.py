from playwright.sync_api import Page


class TodoMvcPage:
    def __init__(self, page: Page):
        self.page = page
        self.new_todo_input = page.locator('.new-todo')
        self.todo_items = page.locator('.todo-list li')

    def open(self):
        self.page.goto('https://demo.playwright.dev/todomvc')

    def add_todo(self, item: str):
        self.new_todo_input.fill(item)
        self.new_todo_input.press('Enter')

    def add_todos(self, items):
        for item in items:
            self.add_todo(item)
