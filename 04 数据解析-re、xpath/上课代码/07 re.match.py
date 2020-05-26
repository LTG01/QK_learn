# 导入模块
import re
# 正则
pattern = 'Python'
# 字符串
string = ' PythonahsdgjasghPythonasdjajsk'
# 匹配
result = re.match(pattern, string)
# 结果
print(result)
# 获取匹配结果的第一个内容
print(result.group(0))
