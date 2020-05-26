import asyncio
import parsel

from pyppeteer import launch

# pyppeteer 这个库是一个异步
# async 拜托别人帮你去做一件事(异步函数需要用 async)
# 异步有时候不靠谱, 但是大部分情况下做比同步又快又好


async def main():
    # launch 启动一个程序
    # 启动的参数给一个字典
    # executablePath 软件存放的地址
    # headless 无头模式,默认是开启的
    browser = await launch({'executablePath': 'D:\\chrome-win\\chrome.exe',
                            'headless': False})
    # 打开一个新的页面
    # 异步里面所有的实践都需要等待事件完成
    page = await browser.newPage()
    # 使用页面请求数据
    await page.goto('http://quotes.toscrape.com/js/')
    # 获取页面的内容
    page_text = await page.content()
    # 使用parsel解析也买你的数据
    selector = parsel.Selector(page_text)
    div_list = selector.css('.quote')
    for div in div_list:
        print(div.extract())
    input()
    await browser.close()


# 事件循环, 异步操作
# 等待不靠谱的朋友,把事情全部做完
asyncio.get_event_loop().run_until_complete(main())
