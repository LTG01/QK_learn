import asyncio
from pyppeteer import launch

width, height = 1366, 768


async def main():
    exe_path = 'C:\\zhenxin\\chrome-win\\chrome.exe'
    browser = await launch({'executablePath': exe_path,
                            'headless': False})
    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    await page.goto('https://movie.douban.com/typerank?type_name=%E5%8A%A8%E4%BD%9C&type=5&interval_id=100:90&action=')
    await asyncio.sleep(6)
    # evaluate可以返回js程序的返回值
    dimensions = await page.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    await asyncio.sleep(6)
    print(dimensions)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
