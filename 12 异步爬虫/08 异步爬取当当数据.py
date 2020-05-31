import time

import aiohttp
import asyncio
import parsel

data_list = []


async def fetch(session, url):
    """下载网页数据方法"""
    async with session.get(url) as response:
        # 等到response得到响应数据, 再返回内容
        # 网页的编码
        return await response.text(encoding='gb18030')


async def parser(html):
    sel = parsel.Selector(html)
    lis = sel.css('.bang_list li')
    data = []
    for li in lis:
        title = li.css('.name a::attr(title)').get()
        level = li.css('.star .level span::attr(style)').get()
        data.append([title, level])
    return data


async def download(url):
    # 创建一个会话
    async with aiohttp.ClientSession() as session:
        # 1. 下载html
        html = await fetch(session, url)
        # html_list.append(html)
        #  解析网页数据
        data = await parser(html)
        # print(会占用时间)
        # print(data)
        data_list.append(data)


# 构建需要请求的任务
tasks = [
    asyncio.ensure_future(
        download('http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-{}'.format(
            page))) for page in range(1, 26)
]

start_time = time.time()
# 放到事件循环完成任务
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(*tasks))
print(len(data_list))
print(data_list)
print(time.time() - start_time)
