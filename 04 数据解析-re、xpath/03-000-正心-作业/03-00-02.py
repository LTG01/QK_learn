"""
    使用 css 选择器将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
import parsel
import time

url = 'https://maoyan.com/board/4'
for i in range(0, 101, 10):
    time.sleep(2)
    params = {
        # 0 25 50
        'offset': i,
        'filter': ''
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers)
    # print(response.text)
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

"""
技术：xpath css 正则表达式 （概念）
工具：lxml pyquery re
      bs4
      scrapy.Selector 
      parsel = lxml + pyquery + re
"""
