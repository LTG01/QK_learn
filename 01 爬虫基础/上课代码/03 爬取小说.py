import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# html 字符串的内容
# response 对象
response = requests.get(url='http://www.shuquge.com/txt/8659/31165742.html', headers=headers)
"""
http://www.shuquge.com/txt/8659/31165742.html

http://         超文本传输协议,超文本（图片、视频、音频）
www             服务器的名字www（world wide web）,代表网站服务
shuquge.com     域名
/               网站的根目录
txt/8659        文件存放的位置
31165742.html   文件的名字
"""
# 编码出现了问题
print(response.encoding)
print(response.apparent_encoding)
# 自动设置编码 99.99% 的情况下是没问题的
response.encoding = response.apparent_encoding

html = response.text

print(html)

