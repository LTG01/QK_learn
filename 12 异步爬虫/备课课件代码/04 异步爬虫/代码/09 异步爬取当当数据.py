# 定义请求网页的方法
import asyncio
import time

import aiohttp

from parsel import Selector

data_list = []


async def fetch(session, url):
    """请求网页的方法"""
    # 异步的方法不能直接返回结果 返回的是一个对象
    async with session.get(url) as response:
        # 等待对象执行完毕 得到结果
        return await response.text(encoding='gb18030')


async def parser(html):
    sel = Selector(html)
    lis = sel.css('.bang_list li')
    l = []
    for li in lis:
        name = li.css('.name a::attr(title)').get()
        star = li.css('.star .level span::attr(style)').get()
        l.append([name, star])
    return l


# async yield 挂起
async def download(url):
    # 请求的session
    async with aiohttp.ClientSession() as session:
        # 调用下载网页的方法得到数据
        html = await fetch(session, url)
        # await 相当于激活函数 send
        data = await parser(html)
        data_list.append(data)


# 3. 把对象变成 task 任务，构成一个列表
# 每一个 task 都是一个协程
# 协程之间切换 开销很小
# 只要内存够大
tasks = [
    asyncio.ensure_future(
        download(f'http://bang.dangdang.com/books/bestsellers/01.00.00.00.00.00-recent7-0-0-1-{page}')) for page in
    range(1, 26)
]
start_time = time.time()

# 4. 放到事件循环里面执行
loop = asyncio.get_event_loop()
# gather 传入的需要是task
loop.run_until_complete(asyncio.gather(*tasks))
# 25页数据
# 0.8460805416107178s
print(data_list)
print(len(data_list))
print(time.time() - start_time)

# 异步不好写大型项目
# 发布新闻
# 需要自己写代码 实现自动管理
# 数据分析
# web （前端 后端）
# 前后端不分离全栈
