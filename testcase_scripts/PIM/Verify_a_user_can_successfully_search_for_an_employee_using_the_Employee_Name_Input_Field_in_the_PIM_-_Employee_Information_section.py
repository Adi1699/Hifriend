from playwright.sync_api import Page
from ..framework.pages.LoginPage import LoginPage
from ..framework.utils.actions import Actions
from ..framework.fixtures.baseTest import test, expect

class TestOrangeHRM:
    def test_search_employee(self, page: Page):
        login_page = LoginPage(page)
        actions = Actions(page)

        # Navigate to the login page
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until='networkidle')

        # Click the Login button
        actions.click(page.get_by_role('button', name='Login'))

        # Click the PIM link
        actions.click(page.get_by_role('link', name='PIM'))

        # Type 'Alice' in the search box
        search_box = page.get_by_role('textbox', name='Type for hints...').first
        search_box.press_sequentially('Alice')

        # Click the Search button
        actions.click(page.get_by_role('button', name='Search'))