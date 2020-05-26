"""
    使用 正则表达式 将猫眼 100 的全部电影信息全部提取出来。
    目标网址：https://maoyan.com/board/4?offset=90
    name（电影名）
    star（主演）
    releasetime（上映时间）
    score（评分）
"""
import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    'Host': 'maoyan.com'
}

response = requests.get('https://maoyan.com/board/4?offset=90', headers=headers)
html = response.text
# print(html)
# names = re.findall('<p class="name"><a href="/films/.*?>(.*?)</a></p>', html)
# print(names)
# stars = re.findall('<p class="star">(.*?)</p>', html, re.S)
# print(stars)
# releasetime = re.findall('<p class="releasetime">(.*?)</p>', html, re.S)
# print(releasetime)
# score = re.findall('<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', html, re.S)
# print(score)

result = re.findall('<p class="name"><a href="/films/.*?>(.*?)</a></p>.*?<p class="star">(.*?)</p>.*?<p class="releasetime">(.*?)</p>.*?<p class="score"><i class="integer">(.*?)</i><i class="fraction">(.*?)</i></p>', html, re.S)
print(result)
for r in result:
    print("".join(r[-2:]))
