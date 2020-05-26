import asyncio
from pyppeteer import launch


async def main():
    browser = await launch({'executablePath': 'D:\\chrome-win\\chrome.exe',
                            'headless': False,
                            'args': ['--disable-infobars']})
    page = await browser.newPage()
    # 伪装ua
    await page.setUserAgent('xxx')
    await page.goto('https://login.taobao.com/member/login.jhtml?redirectURL=https://www.taobao.com/')
    # 字符串是规避淘宝检测
    await page.evaluate('''() =>{ Object.defineProperties(navigator,{ webdriver:{ get: () => false } }) }''')
    await asyncio.sleep(10)


asyncio.get_event_loop().run_until_complete(main())

"""
使用自动化软件, 模拟人爬取数据
bs4 phantomjs gevent 老古董级别的
"""