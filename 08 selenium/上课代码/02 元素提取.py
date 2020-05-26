from selenium import webdriver

drive = webdriver.Chrome()

url = 'https://www.baidu.com'
drive.get(url)

# 根据css选择器提取元素
# find_element_by_css_selector 通过css选择器找到一个元素
# find_elements_by_css_selector 通过css选择器找到很多个元素
# get getall

# .send_keys 输入内容(标签可以被输入内容才可以使用)
# .clear 清空标签里面的数据
# .click 点击案例

# selenium 的css选择器与之前学的是一样的
# 提取到的内容是浏览器中的对象
#
kw = drive.find_element_by_css_selector('#kw')
kw.clear()
kw.send_keys('青灯教育-正心')

su = drive.find_element_by_css_selector('#su')
su.click()

input()

drive.quit()

