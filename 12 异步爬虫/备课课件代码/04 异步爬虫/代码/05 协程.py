import asyncio


# 定义函数 async 把函数修饰成异步
# 1. 定义函数对象(事件)
async def hello(name):
    print('hello', name)

# 2. 把函数对象变成协程对象
coroutine = hello('world')

# 3. 把对象变成 task 任务
task = asyncio.ensure_future(hello('world'))

# 4. 放到事件循环里面执行
loop = asyncio.get_event_loop()

# 5. 把任务放到事件循环里面执行
loop.run_until_complete(task)


