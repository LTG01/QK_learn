"""
    open:   操作文件
        mode 模式
        encoding utf-8（Linux） gbk（windows）

    write: 写入数据（只能写入二进制、字符串、数据流的数据）
"""
# utf-8-sig (兼容编码)
# wps office（默认是gbk）
# 二进制的数据是编码的
# f = open('hello.txt', mode='w', encoding='utf-8')
# f.write('hello world !')
# f.close()
# 不管是什么时候都需要加上（二进制不需要加编码）
with open('hello.txt', mode='w', encoding='utf-8') as f:
    f.write('hello world !')
