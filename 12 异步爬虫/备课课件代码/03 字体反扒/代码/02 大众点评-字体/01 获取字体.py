import re

import requests


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Cookie': '_lxsdk_cuid=17254fb1ee9c8-090e10c5952419-5d492f12-510000-17254fb1ee9c8; _lxsdk=17254fb1ee9c8-090e10c5952419-5d492f12-510000-17254fb1ee9c8; _hc.v=9df71d99-e3a3-6070-ae1b-5690f5819773.1590563644; dplet=65b04618e4f3408edfdba31409fe11a8; dper=340b4025e0a5317db526d53e94bdc1507871aa74dca6cac6bc39db6e01dcd928c657e77b8566eb5fa1cbae64da9c59dbfcc23f21c3ec447cbf04952f7128255149b1412206d4a3ea60120c4badec6dc2cf56c11cd4a1f36732a23f1305e32937; ua=%E5%BF%99%E7%A2%8C%E7%9A%84%E8%BA%AF%E4%BD%93; ctu=c4cbf7c8dc53a7adc479157bd67df302fd56561596751baf779b3b34fe422ae2; ll=7fd06e815b796be3df069dec7836c3df; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1590563644,1590577033; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1590577400; _lxsdk_s=17255c76cb4-6e5-1fb-c1e%7C%7C45',
    'Host': 'www.dianping.com'
}

# 请求网页，获取下载数据
url = 'http://www.dianping.com/shop/22314796'
response = requests.get(url, headers=headers)
html = response.text
print(html)
css_url = re.findall('//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?\.css', html)

with open('替换数据之前.html', mode='w', encoding='utf-8') as f:
    f.write(html)

requests


# 下载css文件，获取字体文件
css_response = requests.get('https:' + css_url[0])
print(css_response.request.url)
css_response.encoding = css_response.apparent_encoding
print(css_response.text)

# 取css文件里面匹配字体的下载链接
font_url = re.findall('@font-face\{font-family: "PingFangSC-Regular-review";.*?format.*?,url\("(.*?)"\);\}', css_response.text)
font_url = font_url[0]
font_name = font_url.split('/')[-1]

# 下载并保存字体文件
font_response = requests.get('https:' + font_url)
print(font_response)
with open(font_name, mode='wb') as f:
    f.write(font_response.content)
