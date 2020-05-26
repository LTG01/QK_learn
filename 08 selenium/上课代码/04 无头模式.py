from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# 淘宝反扒
chrome_options = Options()
chrome_options.add_argument('--headless')

drive = webdriver.Chrome(chrome_options=chrome_options)

url = 'https://www.baidu.com'
drive.get(url)
# 网络不好, 页面没有渲染完
# 动态加载页面, 只有页面加载完之后才会有数据
# 10秒钟之前渲染完,提前结束
drive.implicitly_wait(10)

# 显示等待 死等
# time.sleep(10)

kw = drive.find_element_by_css_selector('#kw')
kw.clear()
kw.send_keys('青灯教育-正心')

su = drive.find_element_by_css_selector('#su')
su.click()

input()
# 所有事情做完之后,在关闭窗口
drive.quit()
