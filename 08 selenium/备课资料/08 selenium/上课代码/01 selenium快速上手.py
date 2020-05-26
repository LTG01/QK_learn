# 切换为国内源
from selenium import webdriver

# web 浏览器 driver 驱动

# 获取chrome的驱动
# 一定要配置驱动 要适配浏览器的版本
drive = webdriver.Chrome(executable_path='chromedriver.exe')

# 使用电脑的浏览器启动百度
url = 'https://www.baidu.com'
drive.get(url)

# 延迟
input()
# 用完之后立马关闭
drive.quit()

# 1. pip install selenium
# 2. 配置浏览器驱动
# 3. 使用 selenium 实例驱动对象，通过对象控制浏览器
