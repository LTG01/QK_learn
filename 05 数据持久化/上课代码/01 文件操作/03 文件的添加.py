"""
    a   添加内容到文件末尾
    +   给最高的权限（可读可写）
"""
with open('hello.txt', mode='a+', encoding='utf-8') as f:
    f.write('hello flask !\n')
