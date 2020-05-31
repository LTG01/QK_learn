import aiohttp
import asyncio


async def fetch(session, url):
    # 爬取数据的方法
    async with session.get(url) as response:
        # await 等待数据返回
        # send
        return await response.text()


async def main():
    # requests.session
    async with aiohttp.ClientSession() as session:
        # 调用异步请求方法,请求数据
        html = await fetch(session, 'http://www.baidu.com')
        print(html)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
