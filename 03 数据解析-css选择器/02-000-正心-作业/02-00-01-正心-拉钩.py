"""
请求拉勾网 python 第一页的招聘数据，并将信息写入到一个txt文本里面。
(温馨提示：速度不要太快，小心被封)

需求1：获取一下信息
    'city': 城市
    'companyFullName': 公司名
    'companySize': 公司规模
    'education': 学历
    'positionName': 职位名称
    'salary': 薪资
    'workYear': 工作时间

需求2：以逗号（,）分割信息内容，写入文件。要求文件名为 `拉钩职位信息.csv`。
例如：
    上海,上海沸橙信息科技有限公司,150-500人,本科,python,8k-12k,不限
"""
# 1. 获取可以用的cookies
import pprint

import requests


def get_cookie():
    headers = {
        'origin': 'https://www.lagou.com',
        'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        'authority': 'www.lagou.com',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    }
    response = requests.get("https://www.lagou.com/jobs/list_python/p-city_3?px=default", headers=headers)
    return response.cookies.get_dict()

# 2. 爬取拉钩招聘数据

url = 'https://www.lagou.com/jobs/positionAjax.json'
params = {
    'city': '上海',
    'needAddtionalResult': 'false'
}
data = {
    "first": "true",
    "pn": "1",
    "kd": "python"
}

headers = {
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'authority': 'www.lagou.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}

cookies = get_cookie()
response = requests.post(url,
                         params=params,
                         data=data,
                         headers=headers,
                         cookies=cookies)
dict_data = response.json()
# pprint.pprint(dict_data)
# 3. 解析数据

results = dict_data['content']['positionResult']['result']
for result in results:
    d = {}
    d['city'] = result['city']
    d['companyFullName'] = result['companyFullName']
    d['companySize'] = result['companySize']
    d['education'] = result['education']
    d['positionName'] = result['positionName']
    d['salary'] = result['salary']
    d['workYear'] = result['workYear']
    print(d)
    with open('拉钩职位信息.csv', mode='a', encoding='utf-8') as f:
        f.write(",".join(d.values()))
        f.write('\n')  # 换行符
# alt + 回车
