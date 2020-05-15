# requests
import requests

# as 重命名
# 响应体
# 使用requests模拟浏览器一样的参数，发送请求就能得到数据
response = requests.get('https://www.baidu.com/')

# 打印响应体对象 属性, 方法
# .status_code 对象的属性
print(response.status_code)
# text
print(response.text)
print(response.request.headers)
