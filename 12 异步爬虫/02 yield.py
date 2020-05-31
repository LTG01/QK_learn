def foo():
    # 可以在一个函数里面进行切换
    for i in range(5):
        # 与return差不多,但是是分为多次返回
        result = yield i  # 返回一个数据,把函数暂时挂起
        print(result)


# def func():
#     l = []
#     for i in range(5):
#         l.append(i)
#     return l


g = foo()
# print(list(g))

# for i in g:
#     print(i)
# 生成器(协程)
# print(next(g))
# print(next(g))
# print(next(g))
# 由下面的代码进行控制
print(g.send(None))
one = g.send('第一次send')
print(one)
two = g.send('第二次send')
print(two)
