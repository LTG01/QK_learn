def foo():
    for i in range(5):
        # yield 挂起(暂停)
        print('yield 返回内容之前')
        # return 返回结果
        # yield 挂起 返回的是迭代规则
        result = yield i  # 把程序暂时挂起,也可以接受激活传递进来的内容
        print('yield 返回内容之后', result)


# 生成器对象 可迭代对象
g = foo()

# print(next(g))
# send 激活函数
# 激活函数第一个内容必须传递 None
print(g.send(None))
# print(g.send('A'))
# print(g.send('B'))
# print(g.send('C'))
# print(g.send('C'))
# print(g.send('C'))
