"""
    使用 xpath 将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
from lxml import etree

headers = {
    'user-agent': '/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


for i in range(10):
    url = 'https://maoyan.com/board/4?offset={}'.format(i*10)
    # url = 'https://movie.douban.com/top250?start={}'.format(i*25)
    res = requests.get(url=url,headers=headers)

    html =etree.HTML(res.text)
    dds = html.xpath('//*[@id="app"]/div/div/div[1]/dl/dd')
    for li in dds:
        name = li.xpath('./a/@title')[0]
        releasetime = li.xpath('./div/div/div[1]/p[3]/text()')[0].split('：')[1]

        score = li.xpath('./div/div/div[2]/p/i[1]/text()')[0][0]
        star = li.xpath('./div/div/div[1]/p[2]/text()')[0].strip()
        print(name,score,star,releasetime)