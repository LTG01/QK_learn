def foo():
    for i in range(5):
        # return i
        # yield 返回的是 generator（生成器）
        yield i


g = foo()
# print(list(g))
# next 迭代一个内容出来
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
for i in g:
    print(i)
