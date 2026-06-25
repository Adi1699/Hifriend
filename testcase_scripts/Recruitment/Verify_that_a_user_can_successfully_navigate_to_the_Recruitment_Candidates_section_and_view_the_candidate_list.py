# === REQUIRED IMPORTS ===
import pytest
from playwright.async_api import async_playwright
from core.base_page import BasePage
from utils.actions import Actions
from pages.login_page import LoginPage

# ----------------------------------------

@pytest.mark.asyncio
async def test_login_and_view_candidates(page):
    login_page = LoginPage(page)
    
    # Open login page
    await login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    
    # Perform login
    await login_page.login("Admin", "admin123")
    
    # Navigate to candidates page
    await login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    await page.wait_for_load_state(state='load')
    
    # Click on the first button in the candidates page
    actions = Actions(page)
    element = page.locator('xpath=html/body/div/div/div[2]/div[2]/div/div[2]/div/button').nth(0)
    await actions.click(element)
    
    # Wait for 2 seconds
    await page.wait_for_timeout(2000)
    
    # Reload candidates page
    await login_page.open("https://opensource-demo.orangehrmlive.com/web/index.php/recruitment/viewCandidates")
    await page.wait_for_load_state(state='load')