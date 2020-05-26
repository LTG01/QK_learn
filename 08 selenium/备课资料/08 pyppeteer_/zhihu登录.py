import asyncio
from pyppeteer import launch
from pyppeteer import launcher
from pyquery import PyQuery as pq
import time

launcher.AUTOMATION_ARGS.remove("--enable-automation")


async def main():
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False,
                            'slowMo': 30,
                            'dumpio': True,
                            'autoClose': False})
    page = await browser.newPage()
    # page.waitForNavigation({'timeout': 1000 * 30})
    await page.goto('https://www.zhihu.com/')
    await page.setViewport({'width': 1366, 'height': 768})

    doc = pq(await page.content())
    print('Quotes:', doc('.quote').length)
    # time.sleep(20)
    await page.click(
        selector='#root > div > main > div > div > div > div.SignContainer-content > div > form > div.SignFlow-tabs > div:nth-child(2)')
    await page.type(selector='div.SignFlow-account > div > label > input', text='17685287506')
    await page.type(selector='div.SignFlow-password > div > label > input', text='218347800wei')
    await page.click(selector='div.SignContainer-content > div > form > button')
    await page.waitForSelector(selector=' div.AppHeader-inner > div.SearchBar > button')
    page_text = await page.content()
    print(page_text)
    # page.title()
    # page.cookies()
    # page.querySelector()
    # page.click()
    # await browser.close()


asyncio.get_event_loop().run_until_complete(main())
