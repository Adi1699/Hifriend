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
            pass

        await page.get_by_role('textbox', name='Username').fill("Admin")

        await page.get_by_role('textbox', name='Password').fill("admin123")

        await page.get_by_role('button', name='Login').click()
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass

        await page.get_by_role('link', name='Admin').click()
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass

        await page.get_by_role('row', name=' Jobinsam@6742 ESS Jobin Sam').get_by_role('button').first.click()
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass

        element = page.locator('xpath=html/body/div/div[3]/div/div/div/div[3]/button').nth(0)
        await element.click()
        await page.wait_for_timeout(2000)

        await browser.close()

asyncio.run(run())