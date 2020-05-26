from selenium import webdriver
# import time
# selenium 自动化测试（pc 浏览器 android ios）
drive = webdriver.Chrome(executable_path='chromedriver.exe')

url = 'https://www.jd.com/'
drive.get(url)
# 默认的情况下会等待加载页面

# 显示等待10秒，十秒之内没有出现
# 语法错误 逻辑

# 固定等待10秒
# time.sleep(10)

# 最多等待 代码优化
drive.implicitly_wait(10)

click_button = drive.find_element_by_css_selector('#search button.button1')
print(click_button)
input()

drive.quit()
