from selenium import webdriver
import time

drive = webdriver.Chrome(executable_path='../chromedriver.exe')

url = 'https://music.163.com/#/playlist?id=924680166'
drive.get(url)

# 切换操作页面
drive.switch_to.frame(0)


# 网易云音乐评论
# 先获取评论标签
# 覆盖掉了selenium里面的关键字
def parser1(drive):
    """
    一旦代码重复使用
    传入值，返回
    """
    data = []
    # 直接获取网页元素
    elements = drive.find_elements_by_css_selector('.itm')
    for element in elements:
        cnt = element.find_element_by_css_selector('.cnt')
        t = element.find_element_by_css_selector('.time')
        data.append([cnt.text, t.text])
    return data


# 执行js代码 下拉滚动条
# 执行js

js = 'window.scrollBy(0, 8000)'
drive.execute_script(js)

# 点击下一页
# 切换 iframe
for i in range(5):
    print(parser1(drive))
    drive.find_element_by_css_selector('.znxt').click()
    time.sleep(1)
# data = parser(drive)
# print(data)
# selenium 整个页面的html
input()
drive.quit()
