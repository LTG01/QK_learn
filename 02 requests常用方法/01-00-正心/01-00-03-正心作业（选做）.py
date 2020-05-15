"""
上课爬取图片的案例
一次性将三张图片全部爬取下来
"""
"""清下下方开始编写代码"""
import re
import requests

index_url = 'http://www.win4000.com/meinv197522_{}.html'
for i in range(1, 4):
    response = requests.get(index_url.format(i))
    r = re.findall(
        '<img class="pic-large" src="http://static.win4000.com/home/images/placeholder.jpg" data-original="(.*?)" url=".*?" />',
        response.text, re.S)
    image_url = r[0]

    image_response = requests.get(image_url)
    image_name = image_url.split('/')[-1]

    # 图片 视频 音频 都是二进制 暂时先记住
    with open(image_name, mode='wb') as f:
        # content 内容
        f.write(image_response.content)

# ctrl + x
