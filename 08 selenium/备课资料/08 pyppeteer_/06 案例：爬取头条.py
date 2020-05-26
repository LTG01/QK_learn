import asyncio
from pyppeteer import launch
import parsel


async def main():
    # headless参数设为False，则变成有头模式
    browser = await launch(
        {'executablePath': 'C:\\zhenxin\\chrome-win\\chrome.exe',
         'headless': False}
    )

    page1 = await browser.newPage()
    # 设置页面视图大小
    await page1.setViewport(viewport={'width': 1280, 'height': 800})
    # 是否启用js


    page2 = await browser.newPage()
    await page2.setViewport(viewport={'width': 1280, 'height': 800})
    await page2.goto('https://news.163.com/domestic/')
    await page2.evaluate('window.scrollTo(0,document.body.scrollHeight)')
    page_text1 = await page2.content()

    await browser.close()

    return {'wangyi': page_text1}


def parse(task):
    content_dic = task.result()

    wangyi = content_dic['wangyi']

    selector = parsel.Selector(wangyi)
    div_list = selector.xpath('//div[@class="data_row news_article clearfix "]')
    print(len(div_list))
    for div in div_list:
        title = div.xpath('.//div[@class="news_title"]/h3/a/text()')[0]
        print('wangyi:', title)


tasks = []
task1 = asyncio.ensure_future(main())
task1.add_done_callback(parse)
tasks.append(task1)
asyncio.get_event_loop().run_until_complete(asyncio.wait(tasks))
