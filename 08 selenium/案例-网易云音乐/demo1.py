# 采集网易云音乐的评论: https://music.163.com/#/song?id=574566207
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
# chrome_options.add_argument('--headless')

# 无头模式内存暂用小, 还不会被干扰
driver = webdriver.Chrome(chrome_options=chrome_options,
                          executable_path="C:\\Users\\Administrator\\Desktop\\08 selenium\\chromedriver.exe")

# 打开网页
driver.get('https://music.163.com/#/song?id=574566207')
# driver.implicitly_wait(10)
time.sleep(10)
html = driver.page_source
print(html)
# 使用selenium采集数据, 获取网页源代码之后用其他方式解析网页数据
