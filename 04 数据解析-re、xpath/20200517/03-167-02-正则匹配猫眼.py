"""
    使用 正则表达式 将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
import parsel
import re

headers = {
    'user-agent': '/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'
}


for i in range(10):
    url = 'https://maoyan.com/board/4?offset={}'.format(i*10)
    # url = 'https://movie.douban.com/top250?start={}'.format(i*25)
    res = requests.get(url=url,headers=headers).text

    # print(res)
    stars= re.findall('''<p class="star">
                (.*?)
        </p>''',res,re.S)
    # print(len(stars),stars)
    releasetimes = re.findall('<p class="releasetime">上映时间：(.*?)</p>    </div>',res,re.S)
    # print(len(releasetimes),releasetimes)
    scores = re.findall('<i class="integer">(.*?).</i>',res,re.S)
    # print(len(scores),scores)
    names = re.findall('<p class="name"><a href="/films/.*?" title="(.*?)" data-act="boarditem-click" data-val="{movieId:',res,re.S)
    # print(len(names),names)

    for i in range(len(names)):
        print(names[i],scores[i],stars[i],releasetimes[i])


