"""
    使用 css 选择器将豆瓣 250 的全部电影信息全部提取出来。
    目标网址：https://movie.douban.com/top250
    title（电影名）
    info（导演、主演、出版时间）
    score（评分）
    follow（评价人数）
    基础、没有用心看内容
"""
import requests
import parsel
import time

url = 'https://movie.douban.com/top250'
for i in range(0, 251, 25):
    time.sleep(2)
    params = {
        # 0 25 50
        'start': i,
        'filter': ''
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    response = requests.get(url, params=params, headers=headers)
    # print(response.text)
    selector = parsel.Selector(response.text)

    li_s = selector.css('ol.grid_view li')
    for li in li_s:
        title = li.css('.info .hd .title::text').get()
        print(title)
        info = li.css('.info .bd p::text').get()
        print(info.strip())
        score = li.css('.rating_num::text').get()
        print(score.strip())
        # 给 get 之后就是字符串了
        follow = li.css('.star span::text')[-1].re('\d+')[-1]
        print(follow.strip())
