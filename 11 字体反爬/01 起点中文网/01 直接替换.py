# ctrl + alt + l 快速格式化代码
import requests

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}
response = requests.get('https://book.qidian.com/info/1013562540', headers=header)

with open('替换之前的.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)

map_dict = {
    '&#100276;': '2',
    '&#100268;': '5',
    '&#100274;': '3',
    '&#100266;': '.',
    '&#100275;': '8',
}

with open('替换之前的.html', mode='r', encoding='utf-8') as f:
    text = f.read()

for key, value in map_dict.items():
    text = text.replace(key, value)

with open('替换之后的.html', mode='w', encoding='utf-8') as f:
    f.write(text)
