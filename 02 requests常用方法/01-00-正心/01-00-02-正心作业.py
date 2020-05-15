"""
先把上课爬取图片的案例练习一遍，再完成下面作业

表情包爬取
将此页面下的前十页图片全部获取下来：https://fabiaoqing.com/biaoqing
"""
import requests
import re

"""清下下方开始编写代码"""
# https://fabiaoqing.com/biaoqing/lists/page/4.html
fmt_url_str = 'https://fabiaoqing.com/biaoqing/lists/page/{}.html'
response = requests.get(fmt_url_str.format(1))
print(response.text)
results = re.findall('<img class="ui image lazy" data-original="(.*?)" .*? title="(.*?)"', response.text, re.S)
print(results)
for url, name in results:
    print(url, name)
    suffix = url.split('.')[-1]
    response = requests.get(url)
    with open(name + '.' + suffix, mode='wb') as f:
        f.write(response.content)
