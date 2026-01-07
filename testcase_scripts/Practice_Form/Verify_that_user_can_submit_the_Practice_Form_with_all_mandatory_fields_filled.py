import asyncio
from playwright.async_api import async_playwright

async def run():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto('https://demoqa.com/')
        await page.wait_for_load_state(state='load')
        element = page.locator('xpath=html/body/div[2]/div/div/div[2]/div/div[2]').nth(0)
        await element.click()
        await page.wait_for_timeout(2000)

        await browser.close()

if __name__ == "__main__":
    asyncio.run(run())