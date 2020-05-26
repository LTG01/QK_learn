# encoding:utf-8
import time
from selenium import webdriver

# 初始化浏览器
driver = webdriver.Chrome()

url = 'https://music.163.com/#/song?id=574566207'
# 打开网址
driver.get(url)
# 切入框内
driver.switch_to.frame(0)
for n in range(5):
    # 下拉混动条
    js = 'window.scrollBy(0, 8000)'
    driver.execute_script(js)

    time.sleep(1)
    #
    # # 选元素
    # elememts = driver.find_elements_by_css_selector('div.cmmts .itm')
    # # 循环遍历
    # for e in elememts:
    #     try:
    #         print(e.find_element_by_css_selector('.f-brk').text)
    #     except:
    #         pass
    # 翻页
    driver.find_element_by_partial_link_text('下一').click()
    time.sleep(1)  # 暂停1s

driver.quit()
