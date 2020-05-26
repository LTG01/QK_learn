"""
使用selenium或者pyppeteer访问下面这个网站
https://www.wjx.cn/jq/78696684.aspx

1. 将所有的单选题随机选择
2. 所有的多选题随机选择两个
3. 填空题随便填入一句话
4. 点击提交按钮之前,让人进行选择是否提交
"""

from selenium import webdriver
import random
import time

url ='https://www.wjx.cn/jq/78696684.aspx'
chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
chrome_options.add_argument('--headless')  # //增加无界面选项
chrome_options.add_argument('--disable-gpu')  # //如果不加这个选项，有时定位会出现问题

driver = webdriver.Chrome()
driver.get(url=url)

driver.implicitly_wait(10)

#confirm("上联：一但重泥拦子路；下联：两岸夫子笑颜回"); //在页面上弹出确认对话框

driver.execute_script('window.confirm("是否提交！");')
time.sleep(5)
s= driver.switch_to.alert.accept()
print(s)

time.sleep(2)

sub = driver.find_element_by_css_selector('.submitbutton')

sub.click()


time.sleep(2)
driver.quit()
# print(len(lilist))