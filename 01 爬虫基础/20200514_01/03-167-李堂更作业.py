"""
上课爬取图片的案例
一次性将三种图片全部爬取下来
"""

import requests
import re
from lxml import etree

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

#每个图片的首页，即可下载所有的
url='http://www.win4000.com/meinv197522_1.html'

# url = 'http://www.win4000.com/meinv197521.html'

if '_' in url:
    url=url[:url.rfind('_')]+'.html'
    print(url)

response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
html = response.text
num = re.findall('</span>/<em>(.*?)</em>）</div>',html)[0]
print(num)
name= re.findall('<div class="ptitle"><h1>(.*?)</h1>',html)[0]



for i in range(1,int(num)+1):

    imgurl = url[:-5]+'_'+str(i)+'.html'
    print(imgurl)
    response = requests.get(imgurl,headers=headers)
    response.encoding=response.apparent_encoding
    html = etree.HTML(response.text)
    durl=html.xpath('//*[@id="pic-meinv"]/a/img/@data-original')[0]

    res=requests.get(url=durl).content
    with open('{}{}.jpg'.format(name,i), 'wb') as f:
        f.write(res)