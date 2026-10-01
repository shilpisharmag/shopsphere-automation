from playwright.sync_api import Page


class TodoMvcPage:
    # Initializes the page objects and all key locators used in the todo app.
    def __init__(self, page: Page):
        self.page = page
        self.new_todo_input = page.get_by_placeholder('What needs to be done?')
        self.todo_list = page.locator('.todo-list')
        self.todo_items = self.todo_list.locator('li')
        self.toggle_all = page.get_by_role('checkbox', name='Mark all as complete')
        self.clear_completed_button = page.get_by_role('button', name='Clear completed')
        self.filter_all = page.get_by_role('link', name='All')
        self.filter_active = page.get_by_role('link', name='Active')
        self.filter_completed = page.get_by_role('link', name='Completed')

    # Opens the TodoMVC application.
    def open(self):
        self.page.goto('https://demo.playwright.dev/todomvc')

    # Adds a single todo item using the UI input field.
    def add_todo(self, item: str):
        self.new_todo_input.fill(item)
        self.new_todo_input.press('Enter')

    # Adds multiple todo items in sequence.
    def add_todos(self, items):
        for item in items:
            self.add_todo(item)

    # Returns the displayed todo item labels.
    def get_todo_texts(self):
        return self.todo_items.locator('label').all_inner_texts()

    #Locates a todo item row by its visible text.
    def get_todo_item(self, text: str):
        return self.todo_items.filter(has_text=text).first

    # Marks a specific todo as completed.
    def complete_todo(self, text: str):
        item = self.get_todo_item(text)
        item.get_by_role('checkbox').check()

    # Edits an existing todo item value.
    def edit_todo(self, old_text: str, new_text: str):
        item = self.get_todo_item(old_text)
        item.locator('label').dblclick()
        edit_field = self.page.locator('.editing .edit')
        edit_field.fill(new_text)
        edit_field.press('Enter')

    # Deletes a todo item from the list.
    def delete_todo(self, text: str):
        item = self.get_todo_item(text)
        item.hover()
        item.locator('.destroy').click()

    # Applies a filter such as All, Active, or Completed.
    def filter_by(self, filter_name: str):
        if filter_name.lower() == 'all':
            self.filter_all.click()
        elif filter_name.lower() == 'active':
            self.filter_active.click()
        elif filter_name.lower() == 'completed':
            self.filter_completed.click()
        else:
            raise ValueError(f'Unsupported filter: {filter_name}')

    # Clears all completed items.
    def clear_completed(self):
        self.clear_completed_button.click()

    # Toggles all todos to the completed state.
    def toggle_all(self):
        self.toggle_all.check()
