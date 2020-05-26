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

lilist=driver.find_elements_by_css_selector('.fieldset .div_question')


for li in lilist:
     time.sleep(1)
     l= li.find_elements_by_css_selector('.ulradiocheck li')
     qtype = li.find_elements_by_css_selector('.div_title_question span')

     if len(qtype)==0:
         text=li.find_element_by_css_selector('#q29')
         text.send_keys('用于测试的')
         pass
     elif len(qtype)==1:

         index = random.randint(0,len(l)-1)

         elementobj= l[index].find_element_by_tag_name('a')
         elementobj.click()

         # driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, 'class', 'jqRadio jqChecked')
         # time.sleep(3)

         pass
     else:

         index = random.sample(range(0,len(l)),2)

         elementobj1= l[index[0]].find_element_by_tag_name('a')
         elementobj1.click()

         # driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, 'class', 'jqCheckbox jqChecked')

         elementobj2 = l[index[1]].find_element_by_tag_name('a')
         elementobj2.click()
         # driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])", elementobj, 'class',
         #                       'jqCheckbox jqChecked')

         # time.sleep(3)

driver.execute_script('alert("是否提交！");')
sub = driver.find_element_by_css_selector('.submitbutton')

sub.click()

# print(len(lilist))