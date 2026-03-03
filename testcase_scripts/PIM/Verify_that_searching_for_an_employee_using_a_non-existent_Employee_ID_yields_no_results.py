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

        element = page.locator('xpath=//input[@name="username" and @placeholder="Username" and contains(normalize-space(@class), "oxd-input")]').nth(0)
        await element.fill('')
        await element.type('Admin')
        await page.wait_for_timeout(2000)
        element = page.locator('xpath=//input[@name="password" and @placeholder="Password" and @type="password" and contains(normalize-space(@class), "oxd-input")]').nth(0)
        await element.fill('')
        await element.type('admin123')
        await page.wait_for_timeout(2000)
        element = page.locator('xpath=html/body/div/div/div/div/div/div[2]/div[2]/form/div[3]/button').nth(0)
        await element.click()
        await page.wait_for_timeout(2000)
        element = page.locator('xpath=//a[@href="/web/index.php/pim/viewPimModule" and contains(normalize-space(@class), "oxd-main-menu-item")]').nth(0)
        await element.click()
        await page.wait_for_timeout(2000)
        element = page.locator('xpath=html/body/div/div/div[2]/div[2]/div/div/div[2]/form/div/div/div[2]/div/div[2]/input').nth(0)
        await element.fill('')
        await element.type('EMP99999')
        await page.wait_for_timeout(2000)
        element = page.locator('xpath=html/body/div/div/div[2]/div[2]/div/div/div[2]/form/div[2]/button[2]').nth(0)
        await element.click()
        await page.wait_for_timeout(2000)

        await browser.close()

asyncio.run(run())