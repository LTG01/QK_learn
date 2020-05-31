import time


def foo1():
    # 可以在一个函数里面进行切换
    while True:
        time.sleep(1)
        # 与return差不多,但是是分为多次返回
        result = yield 'foo1'  # 返回一个数据,把函数暂时挂起
        print(result)


def foo2():

    # 可以在一个函数里面进行切换
    while True:

        # 与return差不多,但是是分为多次返回
        result = yield 'foo2'  # 返回一个数据,把函数暂时挂起
        time.sleep(1)
        print(result)

"""
生成器时协程的实现原理
协程: 可以在线程里面进行切换
"""
# 可回调对象
g1 = foo1()
g2 = foo2()
# 激活生成器
print(g1.send(None))
print(g2.send(None))

while True:
    # 进行协程之间的切换
    print(g1.send("g1"))
    print(g2.send("g2"))
