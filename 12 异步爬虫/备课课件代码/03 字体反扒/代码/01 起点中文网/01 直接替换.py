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

for key, value in map_dict.items():
    old_html.replace(key, value)

