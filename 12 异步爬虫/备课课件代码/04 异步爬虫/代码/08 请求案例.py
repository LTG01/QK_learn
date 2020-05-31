import asyncio
import aiohttp


async def fetch(url):
    async with aiohttp.request('GET', url) as f:
        response = await f.text()
        print(response)
        return response


async def parse(url):
    html = await fetch(url)
    pass
    # 保存 解析


# 3. 把对象变成 task 任务，构成一个列表
tasks = [
    asyncio.ensure_future(parse('https://www.baidu.com/'))
]
# 4. 放到事件循环里面执行
loop = asyncio.get_event_loop()

# gather 传入的需要是task
loop.run_until_complete(asyncio.gather(*tasks))
