import asyncio


# 定义函数 async 把函数修饰成异步
# 1. 定义函数对象(事件)
async def hello(name):
    print('hello', name)


# 2. 把函数对象变成协程对象
coroutine1 = hello('world 1')
coroutine2 = hello('world 2')
coroutine3 = hello('world 3')
coroutine4 = hello('world 4')
coroutine5 = hello('world 5')

# 3. 把对象变成 task 任务，构成一个列表
tasks = [
    asyncio.ensure_future(coroutine1),
    asyncio.ensure_future(coroutine2),
    asyncio.ensure_future(coroutine3),
    asyncio.ensure_future(coroutine4),
    asyncio.ensure_future(coroutine5)
]
# 4. 放到事件循环里面执行
loop = asyncio.get_event_loop()

# 5. 把任务放到事件循环里面执行
# wait 传入的是 tsak 列表
# loop.run_until_complete(asyncio.wait(tasks))
# gather 传入的需要是task
loop.run_until_complete(asyncio.gather(*tasks))

# 知识的迁移能力
