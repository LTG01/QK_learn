from selenium import webdriver

import parsel

url = 'http://www.cnbaowen.net/api/geetest/'

driver = webdriver.Chrome()
driver.get(url)
driver.maximize_window()



hover = driver.find_element_by_css_selector('.gt_slider_knob')

