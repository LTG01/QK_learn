import re

pattern = 'Java'
string = 'Pythonasdkjasd Java adhuiaghsdk Java akjsdhkashdkja'


def func(temp):
    # temp 匹配到的结果
    print(temp)
    print(temp.group(0))
    return "python"


# re.sub 替换字符串
# re.search(匹配结果) + re.findall（匹配到的结果有很多） + str.replace（替换）
# result = re.sub(pattern, "python", string)
# 传入函数对象
result = re.sub(pattern, func, string)
print(result)
