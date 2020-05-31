import re

import requests

map_dict = {
    '&#100432;': '2',
    '&#100423;': '.',
    '&#100430;': '8',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
}

url = 'https://book.qidian.com/info/1013919744'
response = requests.get(url, headers=headers)
old_html = response.text
print(old_html)
with open('old.html', mode='w', encoding='utf-8') as f:
    f.write(old_html)

font_link = re.findall("format\('eot'\); src: url\('(.*?)'\) format\('woff'\)", old_html)
print(font_link)
font_link = font_link[0]
response_woff = requests.get(font_link)
filename = font_link.split('/')[-1]
with open(filename, "wb") as f:
    f.write(response_woff.content)


