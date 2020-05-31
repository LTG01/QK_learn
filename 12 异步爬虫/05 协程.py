# 官方实现的异步库(标准库)
import asyncio


# 所有的异步函数都需要用 async 声明
async def hello(name):
    print('hello', name)


# 把一个异步函数转化为可回调对象
# 协程对象, 需要完成的任务
task = asyncio.ensure_future(hello('world !'))

# 把所有的可对调对象当到时间循环中完成
# 获取时间循环对象
# 事件循环, 发布任务,
loop = asyncio.get_event_loop()
# 把任务放到事件循环里面去, 等待所有的时间全部完成
loop.run_until_complete(task)
