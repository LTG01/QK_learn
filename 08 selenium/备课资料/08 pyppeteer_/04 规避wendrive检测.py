import asyncio
from pyppeteer import launch


async def main():
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False,
                            'args':['--disable-infobars']})
    page = await browser.newPage()
    # 伪装ua
    await page.setUserAgent('xxx')
    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(10)


asyncio.get_event_loop().run_until_complete(main())
