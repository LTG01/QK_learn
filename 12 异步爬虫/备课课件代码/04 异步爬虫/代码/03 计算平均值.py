def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        # 返回平均值
        term = yield average
        # 计算平均值
        total += term
        count += 1
        average = total / count


coro_avg = averager()

next(coro_avg)
# send 传递
print(coro_avg.send(10))
print(coro_avg.send(30))
print(coro_avg.send(5))
print(coro_avg.send(50))
# 协程 在线程里面 不断的切换并且完成任务
