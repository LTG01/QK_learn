"""
爬取网易新闻第一页数据，分别将数据保存为json与csv格式
保存字段需要以下内容

title、channelname、docurl、imgurl、label、source、tlastid、tlink
以及新闻的内容 text

"""

import requests
import parsel
import json
import re


def get_one_page(source_url, query_string, request_headers):
    source_url_response = requests.get(source_url, params=query_string, headers=request_headers)
    source_html = source_url_response.text
    # print(source_html)
    result = re.findall('\[.*\]', source_html, re.S)
    print(result)
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
            'text': parse_url(item['tlink'])
        }
        print(new_item)
        new_items.append(new_item)
    return new_items


def parse_url(page_url):
    page_response = requests.get(page_url)
    page_html = page_response.text
    selector = parsel.Selector(page_html)
    source = selector.css('#content ::text').extract()
    text = "".join(source)
    return text


url = 'https://temp.163.com/special/00804KVA/cm_yaowen20200213.js?'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}

params = {
    'callback': 'data_callback'
}

data = get_one_page(url, params, headers)
with open('data.json', mode='w', encoding='utf-8') as f:
    f.write(json.dumps(data))
# parse_url('http://dy.163.com/v2/article/detail/FCVV90EM0514R9P4.html')
