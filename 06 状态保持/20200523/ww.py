import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.baidu.com")
time.sleep(2)

k = driver.execute_script(" return window.confirm('这是一个alert弹框。');")
driver.implicitly_wait(10)
print('&&&&&')
print(k)
time.sleep(5)
# 接受弹窗，表示点了确定
# driver.switch_to.alert.accept()
# 拒绝弹窗， 表示点了取消
# driver.switch_to.alert.dismiss()

# time.sleep(5)
driver.quit()
