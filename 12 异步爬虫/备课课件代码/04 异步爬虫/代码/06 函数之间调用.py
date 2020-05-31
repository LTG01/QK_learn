import asyncio


# 定义函数 async 把函数修饰成异步
# 1. 定义函数对象(事件)
async def hello(name):
    print('hello', name)


# 2. 把函数对象变成协程对象
# coroutine = hello('world')
async def double_name(name):
    name = name * 2
    # 异步内容之间的函数调用，需要加锁 await 等待
    # return 直接返回结果
    # yield 返回的一个规则 如果是延时操作，可能还没有结果
    r = await hello(name)
    return r


# 3. 把对象变成 task 任务
task = asyncio.ensure_future(double_name('world'))
task2 = asyncio.ensure_future(hello('world'))

# 4. 放到事件循环里面执行
loop = asyncio.get_event_loop()

# 5. 把任务放到事件循环里面执行
loop.run_until_complete(task)
loop.run_until_complete(task2)
