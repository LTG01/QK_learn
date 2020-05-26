from selenium import webdriver

# 下载谷歌浏览器, 下载驱动, 放到当前目录
# 可以指定驱动位置 executable_path="chromedriver.exe"
# 使用 chromedriver驱动  操作浏览器请求数据
# drive 就是浏览器
drive = webdriver.Chrome()

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

# Linux 开发体验最好
# windows 操作最简单
# mac 用户体验最好
