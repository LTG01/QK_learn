import re
# 将正则表达式编译成 Pattern 对象
pattern = re.compile('\d+', re.S)

results1 = re.findall(pattern, '540775360@qq.com')
results2 = re.findall(pattern, "python = 9999， c = 7890， c++ = 12345")
results3 = re.findall(pattern, "python = 997")

print(results1, results2, results3)
