"""
爬取网易新闻第一页数据，分别将数据保存为json与csv格式
保存字段需要以下内容

title、channelname、docurl、imgurl、label、source、tlastid、tlink
以及新闻的内容 text

"""
import csv

import parsel
import requests
import re
import json

url = 'https://temp.163.com/special/00804KVA/cm_yaowen20200213.js'
params = {
    'callback': 'data_callback'
}
headers = {
    "Referer": "https://news.163.com/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}


def parse_url(page_url):
    page_response = requests.get(page_url)
    page_html = page_response.text
    selector = parsel.Selector(page_html)
    source = selector.css('#content ::text').extract()
    text = "".join(source)
    return text


response = requests.get(url=url, headers=headers, params=params)
html = response.text

result = re.findall('data_callback\((.*?)\)', html, re.S)
# print(result[0])
items = json.loads(result[0])
new_items = []
for item in items[:5]:
    new_item = {
        'title': item['title'],
        'channelname': item['channelname'],
        'docurl': item['docurl'],
        'imgurl': item['imgurl'],
        'label': item['label'],
        'source': item['source'],
        'tlastid': item['tlastid'],
        'tlink': item['tlink'],
        'text': parse_url(item['tlink'])  # 下载文章内容
    }
    print(new_item)
    new_items.append(new_item)

print(new_items)

with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json.dumps(new_items, ensure_ascii=False))

with open('data.csv', mode='w', encoding='utf-8', newline="") as f:
    csv_dict_write = csv.DictWriter(f, fieldnames=['title', 'channelname', 'docurl', 'imgurl', 'label', 'source',
                                                   'tlastid', 'tlink', 'text'])
    csv_dict_write.writeheader()
    for item in new_items:
        csv_dict_write.writerow(item)
