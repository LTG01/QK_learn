import time


# 实现功能函数：事件
def foo1():
    while True:
        print('发送请求 1')
        r = yield 'foo1'
        time.sleep(1)
        print('处理得到的数据 1')


def foo2():
    while True:
        print('发送请求 1')
        r = yield 'foo2'
        time.sleep(1)  # time 函数是阻塞 没有释放cpu的使用
        print('处理得到的数据 2')


f1 = foo1()
f2 = foo2()

# 在一个线程里面 交替的完成任务 协程
# 挂起
# 激活
# 请求 等待服务器的返回 处理结果
# 事件循环
"""
1. yield 挂起事件 释放cpu的使用
2. 事件激活 使用
"""
while True:
    print(f1.send(None))
    print(f2.send(None))


