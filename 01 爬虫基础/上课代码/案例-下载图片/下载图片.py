import re

import requests
# 1. 请求网页，得到html
index_url = 'http://www.win4000.com/meinv197522_3.html'
response = requests.get(index_url)
print(response.text)
r = re.findall('<img class="pic-large" src="http://static.win4000.com/home/images/placeholder.jpg" data-original="(.*?)" url=".*?" />', response.text, re.S)
image_url = r[0]

# 2. 从网页中提取 图片下载地址
"""
# 从网页中复制过来的
<img class="pic-large" src="http://pic1.win4000.com/pic/1/81/83e92a68d2.jpg" data-original="http://pic1.win4000.com/pic/1/81/83e92a68d2.jpg" url="http://pic1.win4000.com/pic/1/81/83e92a68d2.jpg" style="display: block;">
# 从 requests 得到的数据里面复制过来的
<img class="pic-large" src="http://static.win4000.com/home/images/placeholder.jpg" data-original="http://pic1.win4000.com/pic/1/81/83e92a68d2.jpg" url="http://pic1.win4000.com/pic/1/81/83e92a68d2.jpg" />
<img class="pic-large" src="http://static.win4000.com/home/images/placeholder.jpg" data-original="(.*?)" url=".*?" />

动态渲染，懒加载 具体情况具体分析
"""


# # 3. 下载图片保存到本地
# image_url = 'http://pic1.win4000.com/pic/1/81/83e92a68d2.jpg'
image_response = requests.get(image_url)
image_name = image_url.split('/')[-1]

# 图片 视频 音频 都是二进制 暂时先记住
with open(image_name, mode='wb') as f:
    # content 内容
    f.write(image_response.content)
