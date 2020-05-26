"""
使用代理爬取猫眼100


代理获取地址: http://134.175.188.27:5010/get/

(可以尝试自己在本地搭建代理池)
"""

import requests
import parsel
import time


def get_proxy():
    response = requests.get('http://134.175.188.27:5010/get/')
    data = response.json()
    proxy = data['proxy']
    print(proxy)

    # 使用代理的参数
    proxies = {
        "http": "http://" + proxy,
        "https": "http://" + proxy,
    }
    return proxies


def download_maoyan(url, params, proxy):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers, proxies=proxy)
    selector = parsel.Selector(response.text)
    li_s = selector.css('.board-wrapper dd')
    for li in li_s:
        name = li.css('.name a::text').get()
        print(name)
        star = li.css('.star::text').get()
        print(star.strip())
        releasetime = li.css('.releasetime::text').get()
        print(releasetime.strip())
        # 给 get 之后就是字符串了
        follow = li.css('.score i::text').getall()
        print(follow)


url = 'https://maoyan.com/board/4?offset={}'
for i in range(0, 101, 10):
    try:
        params = {
            # 0 25 50
            'offset': i,
            'filter': ''
        }
        proxy = get_proxy()

        download_maoyan(url.format(i), params, proxy)
    except:
        params = {
            # 0 25 50
            'offset': i,
            'filter': ''
        }
        proxy = get_proxy()
        download_maoyan(url.format(i), params, proxy)

print(get_proxy())
