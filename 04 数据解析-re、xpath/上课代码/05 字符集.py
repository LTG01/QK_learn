text = """
回复(2)4楼2018-07-04 11:48

哥哥口袋有糖
初识物联1
346504108@qq.com

收起回复5楼2018-07-04 14:10

Super劫Zed: 540775360@qq.com
2018-8-8 16:00回复
我也说一句

RAVV2017
物联硕士4
以上的邮箱，已发，还需要的请回复邮箱。两套物联网学习资料。

回复(4)7楼2018-07-04 16:06

儒雅的刘飞3
初识物联1
0397872410@qq.com，谢谢楼主

收起回复8楼2018-07-04 16:20

RAVV2017: 已发送，麻烦请查收，谢谢
2018-7-4 16:23回复
我也说一句

该来的总会来
物联博士5
1459543548@qq.com
谢谢谢谢

回复9楼2018-07-04 17:18来自Android客户端
BLACKPINK_罗捷
深入物联2
zhengxinonly@qq.com
"""
import re
# 字符集 [] 字符集是一个元字符
result = re.findall('\d+@qq.com', text, re.S)
print(result)
# result = re.findall('[123456789][0123456789]+@qq.com', text, re.S)
# QQ没有用0卡头的 字符集里面没有0
# 不能理解暂时先记住
result = re.findall('[1-9a-z][0-9a-z]+@qq.com', text, re.S)
print(result)
