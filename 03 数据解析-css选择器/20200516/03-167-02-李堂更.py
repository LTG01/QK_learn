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

headers = {
    'user-agent': '/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


for i in range(10):
    url = 'https://maoyan.com/board/4?offset={}'.format(i*10)
    # url = 'https://movie.douban.com/top250?start={}'.format(i*25)
    res = requests.get(url=url,headers=headers)
    selector = parsel.Selector(res.text)
    dds = selector.css('.board-wrapper dd')
    for li in dds:
        star = li.css('.star::text').get().strip()
        releasetime = li.css('.releasetime::text').get()
        score = li.css('.integer::text').get()[0]
        name = li.css('.name a::text').get()
        print(name,score,star,releasetime)