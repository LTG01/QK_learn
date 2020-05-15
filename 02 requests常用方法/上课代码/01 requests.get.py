import requests

url = 'https://image.so.com/i'

# ?q=%E9%A3%8E%E6%99%AF&src=srp&color=yellow
"""
? 前面是请求地址（api）
? 后面都是请求参数
& 每个请求参数之间用&隔开
参数 都是二值性数据 key=value
"""

# 查询参数
params = {
    'q': '风景',
    'src': 'srp',
    # 'color': 'orange',
}
"""
q       关键字，搜索图片的关键字
src     资源，什么类型的图片
color   颜色，过滤的颜色
"""
# 选中之后按 tab 键
# shift+tab 反缩进
# ctrl + 鼠标左键
response = requests.get(url, params=params)

print(response.text)
print(response.url)
# print(response.json())
# ctrl + alt + l （QQ热键冲突）
