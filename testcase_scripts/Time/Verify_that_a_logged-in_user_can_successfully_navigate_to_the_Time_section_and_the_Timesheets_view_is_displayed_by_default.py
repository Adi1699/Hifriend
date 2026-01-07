import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until='domcontentloaded')
        await page.wait_for_load_state('load', timeout=2000).catch(lambda e: None)

        await page.get_by_role('textbox', name='Username').fill("Admin")

        await page.get_by_role('textbox', name='Password').fill("admin123")

        await page.get_by_role('button', name='Login').click()
        await page.wait_for_load_state('load', timeout=2000).catch(lambda e: None)

        await page.get_by_role('link', name='Time').click()
        await page.wait_for_load_state('load', timeout=2000).catch(lambda e: None)

        await browser.close()

asyncio.run(run())