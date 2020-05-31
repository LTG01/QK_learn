"""
分析字体->找到css文件->html

"""
import re

import requests

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    "Host": "www.dianping.com",
    "Cookie": "_lxsdk_cuid=1725af2a84ac8-06675e04d1ade1-3962420d-1fa400-1725af2a84ac8; _lxsdk=1725af2a84ac8-06675e04d1ade1-3962420d-1fa400-1725af2a84ac8; Hm_lvt_602b80cf8079ae6591966cc70a3940e7=1590663752; _hc.v=8f9a884c-928c-8fa5-05e5-829c8b85d444.1590663753; dplet=990cdf7a90cc515eb84e70bf28f76cbb; dper=340b4025e0a5317db526d53e94bdc150f334a5a223f25b94159c07b035a61f528a4ecfd7c89a9b67704a3c4d189d85b51c3b5ef64a7389606be4e4fc058060c1ce9dede82900ec85aa0bb8800d74b36efd38ef5820bac1702c8f572c71f9a98c; ll=7fd06e815b796be3df069dec7836c3df; ua=%E5%BF%99%E7%A2%8C%E7%9A%84%E8%BA%AF%E4%BD%93; ctu=c4cbf7c8dc53a7adc479157bd67df3024343b92d2a8032642426c180b13bd460; Hm_lpvt_602b80cf8079ae6591966cc70a3940e7=1590673569; _lxsdk_s=1725b5d1f66-11d-930-0a6%7C%7C61"" \
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           "}
# 请求html数据
response = requests.get('http://www.dianping.com/shop/22314796', headers=headers)

with open('替换之前.html', mode='w', encoding='utf-8') as f:
    f.write(response.text)
# 获取css的下载地址(字体的下载地址在css文件里面)

css_url = re.findall(
    'type="text/css" href="(//s3plus.meituan.net/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?\.css)"',
    response.text, re.S)
css_content_url = 'https:' + css_url[0]

css_response = requests.get(css_content_url)

# 匹配字体的下载地址
"""
@font-face{font-family: "PingFangSC-Regular-num";src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/788c62d4.eot");src:url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/788c62d4.eot?#iefix") format("embedded-opentype"),url("//s3plus.meituan.net/v1/mss_73a511b8f91f43d0bdae92584ea6330b/font/788c62d4.woff");} 

"""
font_url = re.findall('@font-face\{font-family: "PingFangSC-Regular-review";.*?format.*?,url\("(.*?)"\);\}', css_response.text)

# font_url = re.findall('@font-face\{font-family: "PingFangSC-Regular-review".*?format.*?,url\("(.*?)"\);\}',
#                       css_response.text, re.S)
print(font_url)
font_content_url = 'https:' + font_url[0]
font_response = requests.get(font_content_url)
font_file_name = font_content_url.split('/')[-1]
with open(font_file_name, mode='wb') as f:
    f.write(font_response.content)
