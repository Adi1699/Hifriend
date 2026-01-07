import asyncio
from playwright.async_api import async_playwright, TimeoutError

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until='domcontentloaded')
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass # Equivalent to .catch(() => {}) in JS, ignoring timeout error

        await page.get_by_role('textbox', name='Username').fill("Admin")

        await page.get_by_role('textbox', name='Password').fill("admin123")

        await page.get_by_role('button', name='Login').click()
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass # Equivalent to .catch(() => {}) in JS, ignoring timeout error

        await browser.close()

asyncio.run(run())