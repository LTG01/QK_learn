import requests
import re

header = {
    'Host': 'book.qidian.com',
    'Referer': 'https://www.qidian.com/rank',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.get('https://book.qidian.com/info/1013562540', headers=header)

with open('替换之前的.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)

# 匹配字体文件的下载地址
font_url = re.findall("format\('eot'\); src: url\('(.*?)'\) format\('woff'\)", response.text, re.S)
print(font_url)

font_response = requests.get(font_url[0])
# 从url中取到文件的名字
font_name = font_url[0].split('/')[-1]

with open(font_name, mode='wb') as f:
    f.write(font_response.content)
