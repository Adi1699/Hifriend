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

        await page.get_by_role('textbox', name='用户名').fill("Admin")

        await page.get_by_role('textbox', name='密码').fill("admin123")

        await page.get_by_role('button', name='登录').click()
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass

        await page.get_by_role('link', name='个人信息管理系统').click()
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass

        await page.get_by_role('textbox', name='Type for hints...').first.fill("John Doe")
        await page.get_by_role('textbox', name='Type for hints...').first.press('ArrowDown')
        await page.get_by_role('textbox', name='Type for hints...').first.press('Enter')
        await page.get_by_role('button', name='搜索').click()
        try:
            await page.wait_for_load_state('load', timeout=2000)
        except TimeoutError:
            pass

        await browser.close()

asyncio.run(run())