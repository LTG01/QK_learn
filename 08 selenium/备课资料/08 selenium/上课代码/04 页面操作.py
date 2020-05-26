# -*- coding: utf-8 -*-
"""
点击 & 输入文本动作:
"""
from selenium import webdriver

driver = webdriver.Chrome(executable_path='chromedriver.exe')


url = 'https://www.baidu.com/'
driver.get(url)
# 定位框所在的位置(元素)
search_element = driver.find_element_by_css_selector('#kw')
# 清空标题框内容
search_element.clear()
# 往元素中中传入值 .send_keys('值')
search_element.send_keys('美女')
# 定位点击搜索
click_element = driver.find_element_by_id('su')
# 点击一下
click_element.click()
input()
driver.quit()
