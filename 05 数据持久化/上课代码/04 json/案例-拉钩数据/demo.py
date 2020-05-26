import requests
import json


def get_cookie():
    headers = {
        'origin': 'https://www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'authority': 'www.lagou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }
    response = requests.get("https://www.lagou.com/jobs/list_python/p-city_3?px=default", headers=headers)
    return response.cookies.get_dict()


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
response = requests.post(url,
                         params=params,
                         data=data,
                         headers=headers,
                         cookies=cookies)
html = response.text
print(html)
# str -> dict
# response.json() 调用 json
# data = response.json()
data = json.loads(html)
print(data)
