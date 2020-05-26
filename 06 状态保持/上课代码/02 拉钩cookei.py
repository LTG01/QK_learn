# 1. 获取可以用的cookies
import json
import pprint

import requests


def get_cookie():
    headers = {
        'origin': 'https://www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'authority': 'www.lagou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }
    response = requests.get("https://www.lagou.com/jobs/list_python/p-city_3?px=default", headers=headers)
    return response.cookies.get_dict()

# 2. 爬取拉钩招聘数据

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
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'authority': 'www.lagou.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

cookies = get_cookie()

print(cookies)
with open('cookies.json', mode='w', encoding='utf-8') as f:
    f.write(json.dumps(cookies))

"""
... 省略的意思
"""