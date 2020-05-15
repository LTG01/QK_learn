import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

response = requests.get(url='http://www.shuquge.com/txt/8659/31165742.html', headers=headers)
response.encoding = response.apparent_encoding
html = response.text
print(html)

# 解析数据技术 css、re、xpath > parsel
result = re.findall('<div id="content" class="showtxt">(.*?)</div>', html, re.S)
print(result)
chapter_name = '无巧不成书.txt'
with open(chapter_name, mode='w', encoding='utf-8') as f:
    f.write(result[0].replace('<br/>', '').replace('&nbsp;', ""))

# 每一章下载的地址,名字
