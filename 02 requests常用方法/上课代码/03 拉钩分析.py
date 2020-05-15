import requests

url = 'https://www.lagou.com/jobs/positionAjax.json'
params = {
    'city': '上海',
    'needAddtionalResult': 'false'
}
data = {
    "first": "true",
    "pn": "1",
    "kd": "python"
}

headers = {
    # 原始放在，从哪里来
    'origin': 'https://www.lagou.com',
    # 防盗链，上次请求的网址是哪个
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    # host 主机地址
    'authority': 'www.lagou.com',
    # 用户代理，浏览的版本信息
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    # 问题出在 cookie
    'cookie': 'JSESSIONID=ABAAAECABFAACEA93D9286FED9EB42BB63BE257E4B1F432; SEARCH_ID=7523f4f4ac734b32b0752166dd4497a6; user_trace_token=20200515214524-9cb62c9d-8aef-46d7-8bd0-18645c44c5eb; X_HTTP_TOKEN=42daf4b72327b2814230559851bf5e71415983ed09; WEBTJ-ID=20200515214524-172189519931ea-0538f1e0db3da3-f313f6d-2073600-17218951994364'
}

"""
找到最开始的 cookie 

反扒需要修改cookie

1. 清空浏览器的 cookie (身份信息)
2. 重新请求，服务器会返回 cookie
3. js修改cookie，进行加密

"""
response = requests.post(url,
                         params=params,
                         data=data,
                         headers=headers)
print(response.text)
print(response.request.headers)
# 投毒：服务器返回错误的结果，误导你的判断
