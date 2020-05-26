"""
cookie 是身份信息, 在浏览器中记录登录状态

seesion 会话,保持与服务器整个链接(能记录服务器对cookie的修改)
"""
import time

import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'authority': 'www.lagou.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

# 创建一个会话(自动更新服务器给设置的cookie)
session = requests.Session()

# 请求服务器获取信息
response = session.get("https://www.lagou.com/jobs/list_python/p-city_3?px=default", headers=headers)
print(response.cookies.get_dict())


def get_data(page, sid=None):
    if page == 1:
        return {
            'first': 'true',
            'pn': {page},
            'kd': 'python',
        }
    else:
        return {
            'first': 'false',
            'pn': {page},
            'kd': 'python',
            'sid': sid
        }


sid = None
for page in range(1, 15):
    time.sleep(1)
    data = get_data(page, sid=sid)
    # 使用之前的会话进行请求
    result = session.post(url, data=data, headers=headers)
    print(response)
    print(result.json())
    # sid 是第二次请求必须携带上的参数
    sid = result.json()['content']['showId']


"""
session 维护整个会话过程(服务器修改的 cookies 变化)

selenium 
注册机、自动签到(cookies)
"""
