import requests
import re
from lxml import etree

from selenium import webdriver
#
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

url='https://fabiaoqing.com/biaoqing/lists/page/2.html'

url='http://www.win4000.com/meinv197522_1.html'

print(url[:-5])


response = requests.get(url=url, headers=headers)
response.encoding = response.apparent_encoding
html = response.text
print(html)
tt = re.findall('</span>/<em>(.*?)</em>）</div>',html)[0]
ttt= re.findall('<div class="ptitle"><h1>(.*?)</h1>',html)[0]
print(ttt)
html =etree.HTML(html)

tt= html.xpath('//*[@id="pic-meinv"]/a/img/@data-original')

print(tt)

# chrome_options = webdriver.ChromeOptions()
# # 使用headless无界面浏览器模式
# chrome_options.add_argument('--headless')  # //增加无界面选项
# chrome_options.add_argument('--disable-gpu')  # //如果不加这个选项，有时定位会出现问题
#
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.get('http://www.shuquge.com/txt/8659/31165742.html')
#
# # print(driver.page_source)
#
# text = driver.find_element_by_id('content').text
#
# with open('11.txt','w') as f:
#     f.write(text)

# print(text)