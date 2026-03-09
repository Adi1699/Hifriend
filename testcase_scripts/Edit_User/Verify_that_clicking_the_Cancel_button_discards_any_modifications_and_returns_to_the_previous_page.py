import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login", wait_until='domcontentloaded')
        await page.wait_for_load_state('load', timeout=2000)


        await browser.close()

asyncio.run(run())