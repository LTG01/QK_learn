import requests

url = 'https://www.baidu.com'

headers = {
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'authority': 'www.lagou.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
cookies = {'X_HTTP_TOKEN': '42daf4b72327b2818870559851bf5e71415983ed09',
           'user_trace_token': '20200515215308-17480db5-73c1-4d15-b5ee-64d533e99724',
           'JSESSIONID': 'ABAAABAABAGABFA99B0BFC47767550E0E81969F4F93667D',
           'SEARCH_ID': 'ed64061b92534f7cba1a0a1c90762e9a'}

response = requests.get(url,
                        headers=headers,
                        cookies=cookies)
# 答应响应体的cookie 服务器设置的身份信息
print(response.cookies)
# print(response.request.headers)
"""
apparent_encoding  期待的编码   
cookies            身份信息   	
json               json() 把字典格式的字符串变成字典对象   
encoding           文本内容的编码格式   
content            内容（二进制）   
headers            请求头信息
url                请求的网址
"""
print(response.url)
