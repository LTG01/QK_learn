import time


def foo1():
    # 可以在一个函数里面进行切换
    while True:
        # 与return差不多,但是是分为多次返回
        result = yield 'foo1'  # 返回一个数据,把函数暂时挂起
        time.sleep(10)
        print(result)


# 可回调对象
g1 = foo1()
# 激活生成器
print(g1.send(None))
# 等到生成器返回内容之后才会有数据
print(g1.send("g1"))
print(g1.send("g1"))
print(g1.send("g1"))
print(g1.send("g1"))
"""
send 调用协程,问协程有没有数据了
yield 返回数据
"""
