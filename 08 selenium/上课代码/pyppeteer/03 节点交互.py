import asyncio
from pyppeteer import launch


async def main():
    # headless参数设为False，则变成有头模式
    browser = await  launch(
        {'executablePath': 'D:\\chrome-win\\chrome.exe',
         'headless': False}
    )

    page = await browser.newPage()
    # 设置页面视图大小
    await page.setViewport(viewport={'width': 1280, 'height': 800})

    await page.goto('https://www.baidu.com/')
    # 节点交互 点击 #kw 标签
    await page.type('#kw', '周杰伦', {'delay': 1000})
    await asyncio.sleep(3)
    await page.click('#su')
    await asyncio.sleep(3)
    # 使用选择器选中标签进行点击
    a_list = await page.querySelectorAll('.s_tab_inner > a')
    a = a_list[2]
    await a.click()
    await asyncio.sleep(30)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())