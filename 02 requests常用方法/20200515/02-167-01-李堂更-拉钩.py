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

作业提交格式
    + 使用源代码的方式提交，题目用 `注释` 的方式写在源代码里面。
    + 作业文件命名：第几次作业-编号-作业编号-姓名.py（例如02-00-01-正心.py）
    + 提交作业文件压缩包命名 第几次作业-编号-姓名.zip(例如02-00-正心.zip)
    + 提交到QQ邮箱：2328074219@qq.com
"""

import requests


from copyheaders import headers_raw_to_dict
import csv
import time
import random

def get_cookies():
    headers = '''
authority: www.lagou.com
method: GET
path: /jobs/list_python/p-city_0?
scheme: https
accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
accept-encoding: gzip, deflate, br
accept-language: zh-CN,zh;q=0.9
cache-control: no-cache
pragma: no-cache
sec-fetch-dest: document
sec-fetch-mode: navigate
sec-fetch-site: none
sec-fetch-user: ?1
upgrade-insecure-requests: 1
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
    '''
    h = bytes(headers, encoding="utf-8")
    headers = headers_raw_to_dict(h)
    url = 'https://www.lagou.com/jobs/list_python/p-city_0?'
    response = requests.get(url=url,headers=headers)
    cookies= response.cookies.get_dict()
    # print(cookies)
    # print()
    return cookies



#    cookie: user_trace_token=20200516121447-c75fbdf8-972b-11ea-8008-52540063a8d7; JSESSIONID=ABAAABAABEIABCIF8F30AB92BD8C36409F467165E78830B; SEARCH_ID=876d63a621c14196ae02f5ee3953f6de; X_HTTP_TOKEN=7010a50404777a364942069851c3134a76ac758990; WEBTJ-ID=20200516121454-1721bb1293be49-0359cf206c046e-30677c00-1296000-1721bb1293c835

def get_info_list(page=1):
    headers = '''
   referer: https://www.lagou.com/jobs/list_python/p-city_0?
    user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36

    '''
    h = bytes(headers, encoding="utf-8")
    headers = headers_raw_to_dict(h)

    info_list=[]
    info_list.append(['城市','公司名','公司规模','学历','职位名称','薪资','工作时间'])
    for i in range(1,page+1):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        data = {
            "first": "true",
            "pn": str(i),
            "kd": "python"
        }

        response = requests.post(url,data=data,headers=headers,cookies=get_cookies())
        data = response.json()
        try:
            print(data)
            datalist= data['content']['positionResult']['result']
            for data in datalist:
                city = data['city']
                companyFullName = data['companyFullName']
                companySize = data['companySize']
                education = data['education']
                positionName = data['positionName']
                salary = data['salary']
                workYear = data['workYear']

                info_list.append([city, companyFullName, companySize, education, positionName, salary, workYear])

        except Exception as e:
            print(str(e))
            pass
    return info_list

def save_info(info_list):
    with open('拉钩职位信息.csv', 'w') as f:
        writeCSV = csv.writer(f)
        for info in info_list:
            writeCSV.writerow(info)


if __name__=='__main__':
    # get_cookies()
    infolist = get_info_list(page=3)
    #
    save_info(infolist)
    pass




