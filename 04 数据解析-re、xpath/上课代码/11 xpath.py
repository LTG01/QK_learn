"""
css
直接写标签选择器
> 子节点
# (id选择器) .(类选择器) attr(属性提取器)
多个属性提取 span.name#name

xpath
//name 任意的name节点
/name 子节点
@ 提取属性
//name[@class][@class][@id] 使用艾特符号指定属性进行提取
"""
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
params = {
    # 0 25 50
    'start': 25,
    'filter': ''
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
response = requests.get(url, params=params, headers=headers)
# print(response.text)
selector = parsel.Selector(response.text)

# li_s = selector.css('ol.grid_view li')
li_s = selector.xpath('//ol[@class="grid_view"]/li')
for li in li_s:
    # xpath 二次提取需要从 . 开始提取
    # title = li.css('.info .hd .title::text').get()
    title = li.xpath('.//*[@class="info"]/div[@class="hd"]/a/span/text()').get()
    print(title)
    # info = li.css('.info .bd p::text').get()
    info = li.xpath('//*[@class="info"]//*[@class="bd"]//p/text()').get()
    print(info.strip())
    info_attr = li.xpath('.//*[@class="pic"]/a/@href').get()
    print(info_attr.strip())
