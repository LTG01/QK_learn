# 采集网易云音乐的评论: https://music.163.com/#/song?id=574566207
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument('--headless')

# 无头模式内存暂用小, 还不会被干扰
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="../chromedriver.exe")

# 打开网页
driver.get('https://music.163.com/#/song?id=574566207')

# 切换到评论页面
driver.switch_to.frame(driver.find_element_by_css_selector('#g_iframe'))
for i in range(5):
    driver.implicitly_wait(10)
    div = driver.find_elements_by_css_selector('.cmmts .itm')
    for d in div:
        text = d.find_element_by_css_selector('div.cnt.f-brk').text
        print(text)
    time.sleep(1)
    next_a = driver.find_element_by_css_selector('.znxt')
    next_a.click()
    print('点击了翻页')