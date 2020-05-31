import re

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie': '_lxsdk_cuid=17254fb1ee9c8-090e10c5952419-5d492f12-510000-17254fb1ee9c8; _lxsdk=17254fb1ee9c8-090e10c5952419-5d492f12-510000-17254fb1ee9c8; _hc.v=9df71d99-e3a3-6070-ae1b-5690f5819773.1590563644; dplet=65b04618e4f3408edfdba31409fe11a8; dper=340b4025e0a5317db526d53e94bdc1507871aa74dca6cac6bc39db6e01dcd928c657e77b8566eb5fa1cbae64da9c59dbfcc23f21c3ec447cbf04952f7128255149b1412206d4a3ea60120c4badec6dc2cf56c11cd4a1f36732a23f1305e32937; ua=%E5%BF%99%E7%A2%8C%E7%9A%84%E8%BA%AF%E4%BD%93; ctu=c4cbf7c8dc53a7adc479157bd67df302fd56561596751baf779b3b34fe422ae2; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1590563644,1590577033; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1590577400; _lxsdk_s=17255c76cb4-6e5-1fb-c1e%7C%7C45',
    'Host': 'www.dianping.com'
}

# 先请求网页数据
url = 'http://www.dianping.com/shop/130096343/review_all'
response = requests.get(url, headers=headers)
html = response.text
with open('大众点评-svg.html', mode='w', encoding='utf-8') as f:
    f.write(html)

css_url = re.findall('type="text/css" href="(//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?\.css)"', html)[0]
print(css_url)
css_response = requests.get('https:' + css_url)

css_html = css_response.text
print(css_html)

result = re.findall(
    'background-image: url\((//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?\.svg)\);',
    css_html, re.S)
print(result[1])

svg_response = requests.get('https:' + result[1])
print(svg_response)

# 从css文件中获取需要替换的类名与位置
# print(css_response.text)
# print(len(css_response.text))
pattern = re.compile('.(\w+){background:-(\d+\.\d+)px -(\d+\.\d+)px;}')
class_map = re.findall(pattern, css_response.text)
print(class_map)

coord = class_map[0]

if coord:
    coord_name, coord_x, coord_y = coord
    coord_x, coord_y = float(coord_x), float(coord_y)

import parsel

print(svg_response.text)
svg_data = parsel.Selector(svg_response.text)

texts = svg_data.xpath('//text')
# 根据类名的位置确定y（在哪一行）
print(coord_y)
axis = []
# 那已知点的y去svg表中查询位于哪一行
for text in texts:
    if coord_y <= int(text.attrib.get('y')):
        axis.append(text.attrib.get('y'))

# axis = [text.attrib.get('y') for text in texts if coord_y <= int(text.attrib.get('y'))]
print('axis', axis)
axis_y = axis[0]

print(axis_y)
# 制定y属性获取当前行的某个文字
svg_text_line = svg_data.xpath('//text[@y="%s"]/text()' % int(axis_y)).extract_first()
print('svg_text', svg_text_line)

font_size = re.search('font-size:(\d+)px', svg_response.text).group(1)
print(font_size)
# x位置 求出文字是第几个
x_position = int(coord_x) // int(font_size)
print(coord_name, svg_text_line[x_position])
