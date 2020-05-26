"""
采集地址：https://www.ximalaya.com/youshengshu/16411402/
目标：前三页的所有音频
"""


import requests

from lxml import etree

for i in range(1,4):
    url = 'https://www.ximalaya.com/youshengshu/16411402/p{}'.format(i)

    # url = 'https://www.ximalaya.com/revision/play/v1/audio?id=98791745&ptype=1'

    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36'

    }

    response = requests.get(url,headers=headers)
    html = etree.HTML(response.text)
    urls = html.xpath('//*[@id="anchor_sound_list"]/div[2]/ul/li/div[2]')
    for item in urls:
        id = item.xpath('./a/@href')[0].split('/')[-1]
        name = item.xpath('./a/span/text()')[0].split('（')[0]
        print(name,id)
        url = 'https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1'.format(id)
        response = requests.get(url, headers=headers)
        data = response.json()
        src = data['data']['src']
        response = requests.get(src, headers=headers)
        with open('{}.mp3'.format(name),'wb') as f:
            f.write(response.content)


