"""
cookie 是身份信息, 在浏览器中记录登录状态

seesion 会话,保持与服务器整个链接(能记录服务器对cookie的修改)
"""

import requests

url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'

headers = {
        'origin': 'https://www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'authority': 'www.lagou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }


def get_cookie():
    """获取新的cookie"""
    response = requests.get("https://www.lagou.com/jobs/list_python/p-city_3?px=default", headers=headers)
    return response.cookies.get_dict()


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


# 第一次请求获取一个新的cookie
cookies = get_cookie()
# 获取第一页的请求参数
data = get_data(1)
result = requests.post(url, data=data, headers=headers, cookies=cookies)
print(result.json())
# sid 是第二次请求必须携带上的参数
sid = result.json()['content']['showId']


# 获取一个新的cookie
cookies = get_cookie()
# 获取一个新的参数
data = get_data(2, sid=sid)
result = requests.post(url, data=data, headers=headers, cookies=cookies)
print(result.json())
sid = result.json()['content']['showId']


cookies = get_cookie()
data = get_data(3, sid=sid)
result = requests.post(url, data=data, headers=headers, cookies=cookies)
print(result.json())
sid = result.json()['content']['showId']


cookies = get_cookie()
data = get_data(4, sid=sid)
result = requests.post(url, data=data, headers=headers, cookies=cookies)
print(result.json())
sid = result.json()['content']['showId']


cookies = get_cookie()
data = get_data(5, sid=sid)
result = requests.post(url, data=data, headers=headers, cookies=cookies)
print(result.json())
sid = result.json()['content']['showId']


cookies = get_cookie()
data = get_data(6, sid=sid)
result = requests.post(url, data=data, headers=headers, cookies=cookies)
print(result.json())
sid = result.json()['content']['showId']
