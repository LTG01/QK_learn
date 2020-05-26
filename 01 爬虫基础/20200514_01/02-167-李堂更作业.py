


"""
先把上课爬取图片的案例练习一遍，再完成下面作业

表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""

import requests
from lxml import etree
for i in range(1,11):
    url = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'.format(i)
    response = requests.get(url)
    response.encoding=response.apparent_encoding
    html = etree.HTML(response.text)
    dd = html.xpath('//*[@id="bqb"]/div[1]/div')

    for d in dd:
        durl = d.xpath('./a/img/@data-original')[0]
        name = d.xpath('./a/@title')[0]

        res=requests.get(url=durl).content
        with open('{}.jpg'.format(name), 'wb') as f:
            f.write(res)