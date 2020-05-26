text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com 2018-8-8@qq.c\nom 16:00回复@qq.com
Super劫Zed: 185462874@qq.com 2018-8-8@qq.com 16:00回复@qq.com
Super劫Zed: 245286391@qq.com 2018-8-8@qq.com 16:00回复@qq.com
"""
import re

result = re.findall('Super劫Zed: .*?@qq.com.*?@qq.com', text, re.S)
print(result)
"""
不加括号 是 泛匹配
()      精确匹配，匹配之后进行提取

提取邮箱
"""
result = re.findall('Super劫Zed: (.*?@qq.com)(.*?)@qq.com', text, re.S)
print(result)
for r in result:
    print(r)
