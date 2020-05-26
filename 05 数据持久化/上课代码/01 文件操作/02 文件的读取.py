"""
    r   读取文件
"""
with open('hello.txt', mode='r', encoding='utf-8') as f:
    # text = f.read()
    text = f.readline()
    print(text)
    text = f.readline()
    print(text)
    text = f.readlines()
print(text)