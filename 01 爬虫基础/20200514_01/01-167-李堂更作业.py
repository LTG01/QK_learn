
'''将上课的案例-爬取小说完善。爬取《剑来》所有章节用章节名分别保存。'''
import requests

from lxml import etree
from selenium import webdriver


url = 'http://www.shuquge.com/txt/8659/'

response = requests.get(url)
response.encoding=response.apparent_encoding

html = etree.HTML(response.text)

dd = html.xpath('/html/body/div[5]/dl/dd')

for d in dd[11:]:
    durl = url + d.xpath('./a/@href')[0]
    name = d.xpath('./a/text()')[0]

    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    chrome_options.add_argument('--headless')  # //增加无界面选项
    chrome_options.add_argument('--disable-gpu')  # //如果不加这个选项，有时定位会出现问题

    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get(durl)

    # print(driver.page_source)

    text = driver.find_element_by_id('content').text

    with open('{}.txt'.format(name), 'w') as f:
        f.write(text)