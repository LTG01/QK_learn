import requests

url = 'https://image.so.com/i'

params = {
    'q': '风景',
    'src': 'srp',
}

headers = {
    'user-agent': "asdsadsadasds"
}

# request
response = requests.get(url=url, params=params, headers=headers)
# requests
print(response.request.headers)
"""
request 请求对象
get post delete put .....

method: 请求方法
url: url
params: (可选的) 字典
data: (可选的) 字典

headers: (可选的) 字典 请求头.
cookies: (可选的) Dict or CookieJar object 
proxies: (可选的) 字典 使用代理.

timeout: (可选的) 超时时间主动报错

allow_redirects: (可选的) 布尔.是否允许重定向
verify: 布尔 验证
stream: (可选的) 数据流形式的

ctrl + f 搜索内容
"""

