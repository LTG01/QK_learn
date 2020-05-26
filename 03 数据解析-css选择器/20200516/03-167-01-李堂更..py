"""
    使用 css 选择器将豆瓣 250 的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250
    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
"""

import requests
import parsel

headers = {
    'user-agent': '/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


for i in range(10):
    print(i)
    # url = 'https://movie.douban.com/top250'
    url = 'https://movie.douban.com/top250?start={}'.format(i*25)
    res = requests.get(url=url,headers=headers)
    selector = parsel.Selector(res.text)
    lis = selector.css('.grid_view li')
    for li in lis:
        title = li.css('.title::text').get()
        info = li.css('.bd p::text').getall()[0].strip()
        score = li.css('.rating_num::text').get()
        follow = li.css('.star span::text').getall()[-1]
        print(title,info,score,follow)