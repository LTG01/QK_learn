# 官方实现的异步库 最基本的一些功能
import asyncio
# 第三方库，异步网络请求库
import aiohttp


async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    # 执行的事件
    # aiohttp.ClientSession 客户端的会话
    # aiohttp.ClientSession() 是一个方法
    # 使用 with 调用请求方法，把返回的结果重命名为 session 对象
    async with aiohttp.ClientSession() as session:
        # 调用 fetch 方法
        html = await fetch(session, 'https://www.baidu.com/')
        print(html)


if __name__ == '__main__':
    # 1. 定义事件循环
    loop = asyncio.get_event_loop()
    # 2. 执行事件
    loop.run_until_complete(main())
