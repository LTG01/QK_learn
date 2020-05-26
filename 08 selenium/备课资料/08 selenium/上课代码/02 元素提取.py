from selenium import webdriver

drive = webdriver.Chrome(executable_path='chromedriver.exe')

url = 'https://www.jd.com/'
drive.get(url)


# 1. 获取输入 输入关键字
key_button = drive.find_element_by_css_selector('#key')
key_button.clear()
key_button.send_keys('固态')
# 2. 点击搜索 #search button.button

click_button = drive.find_element_by_css_selector('#search button.button')
click_button.click()
# 阻塞之后 在浏览器中进行

print(drive.get_cookies())

# selenium 开发简单

# 爬虫 爬取数据   采集数据
# selenium 自动化 模拟人为操作
# cookie

"""css选择器选择标签"""
# key_button = drive.find_element_by_css_selector('#key')
# key_button.clear()
# key_button.send_keys('固态')
#
# click_button = drive.find_element_by_css_selector('#search button.button')
# click_button.click()

"""xpath节点提取"""
# key_button = drive.find_element_by_xpath('//*[@id="key"]')
# key_button.clear()
# key_button.send_keys('固态')
#
# click_button = drive.find_element_by_css_selector('//*[@id="search"]//button[@class="button"]')
# click_button.click()

input()
drive.quit()
