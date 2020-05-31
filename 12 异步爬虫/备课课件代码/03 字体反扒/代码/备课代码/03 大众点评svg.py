import requests
import re

import numpy
from PIL import Image, ImageFont, ImageDraw
import pytesseract
import requests
from fontTools.ttLib import TTFont

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3970.5 Safari/537.36",
    'Referer': 'http://www.dianping.com/shop/43775428',
    'Cookie': '_lxsdk_cuid=1704ff33901c8-0fc6f4bb8331ae-366b420b-7e9000-1704ff33901c8; _lxsdk=1704ff33901c8-0fc6f4bb8331ae-366b420b-7e9000-1704ff33901c8; _hc.v=b04f69fc-3c80-4008-5839-bf96c74c7572.1581889305; dplet=a9800db2dfb4c48994773498927732b6; dper=3a3c23b40e1f6ddc6aa0d31ab68de7c4c64e8968e260752b18380fadb969c536601ff8ebe9f432b765555fc9d8f7c11810ccda14e579f0bd721376f0361a78a1df715dcc09b3effac0af278c0af2f60aaef65401f5243049d669413beeb744fc; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%BF%99%E7%A2%8C%E7%9A%84%E8%BA%AF%E4%BD%93; ctu=c4cbf7c8dc53a7adc479157bd67df302d8cf2cd7afdb00064575dd4b5a28b72f; _lxsdk_s=1704ff33902-dbc-8a7-1b4%7C%7C28'

}


def get_response(url):
    resp = requests.get(url, headers=header)
    return resp

if __name__ == '__main__':
    url = 'http://www.dianping.com/shop/130096343/review_all'
    response = get_response(url)
    html = response.text
    print(html)

    css_url = re.findall('type="text/css" href="(//s3plus.sankuai.com/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?.css)"', html)[0]
    print(css_url)
    css_response = get_response('https:'+css_url)
    #
    svg_url = re.findall('background-image: url\((//s3plus.sankuai.com/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?.svg)\);', css_response.text)
    # print(svg_url)
    svg_response = get_response('https:'+svg_url[-1])
    print(svg_url)

    # 获取需要替换的类名与位置
    print(css_response.text)
    print(len(css_response.text))
    pattern = re.compile('.(\w+){background:-(\d+\.\d+)px -(\d+\.\d+)px;}')
    class_map = pattern.findall(css_response.text)
    print(class_map)

    coord = class_map[0]

    if coord:
        coord_name, coord_x, coord_y = coord
        coord_x, coord_y = float(coord_x), float(coord_y)

    from parsel import Selector

    svg_data = Selector(svg_response.text)

    texts = svg_data.xpath('//text')
    # for text in texts:
    #     if coord_y <= int(text.attrib.get('y')):
    #         axis_y = text.attrib.get('y')
    axis = [text.attrib.get('y') for text in texts if coord_y <= int(text.attrib.get('y'))]
    print('axis', axis)
    axis_y = axis[0]
    print(axis_y)
    # 获取当前行文字
    svg_text = svg_data.xpath('//text[@y="%s"]/text()' % int(axis_y)).extract_first()
    print('svg_text', svg_text)
    print(svg_text)
    font_size = re.search('font-size:(\d+)px', svg_response.text).group(1)
    print(font_size)
    position = int(coord_x) // int(font_size)
    print(svg_text[position])
