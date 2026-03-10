import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://opensource-demo.orangehrmlive.com/web/index/auth/login", wait_until='networkidle')


        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())