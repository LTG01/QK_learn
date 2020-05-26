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
"""
.* 可以匹配所有的字符（但是不能匹配空白字符）
默认情况下是贪婪模式 

? 非贪婪匹配的标志
"""
# 在 re.S 模式下 . 可以特殊的空白字符
result = re.findall('Super劫Zed: .*?@qq.com.*?@qq.com', text, re.S)
print(result)
# 找不到就没有结果
