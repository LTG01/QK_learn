import re

# 匹配规则
pattern = '\d{11}'
# 替换目标
repl = '***********'
# 字符串
string = """
18654924151
18123412442
14561231324
18678941526
18123115458
"""


def func(temp):
    str_ = temp.group(0)
    return str_[:3] + "****" + str_[-3:]


result = re.findall(pattern, string, re.S)
print(result)

result = re.sub(pattern, func, string, re.S)
print(result)
