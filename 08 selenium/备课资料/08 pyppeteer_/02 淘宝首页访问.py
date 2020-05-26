import asyncio
from pyppeteer import launch


async def main():
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False})
    page = await browser.newPage()
    await page.setViewport({'width': 1366, 'height': 768})
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(10)


asyncio.get_event_loop().run_until_complete(main())
