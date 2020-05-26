"""
    请求拉勾网 python 前十页的招聘数据，并将信息写入到一个txt文本里面。
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
import requests

# 爬取的url
url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'


# data
def data(page):
    return {
        "first": "true",
        "pn": f"{page}",
        "kd": "python",
        'sid': '4256fece2141497bb5a8e1bfa69bcee7'
    }


# 请求头
headers = {
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'
}


# 获取cookies
def get_cookies():
    return requests.get('https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
                        headers=headers).cookies.get_dict()


# cookies
cookies = get_cookies()


def get_data(data):
    response = requests.post(url=url, headers=headers, data=data, cookies=cookies)
    # json数据
    content = response.json()['content']['positionResult']['result']
    j = 1

    for i in content:
        city = i['city']
        companyFullName = i['companyFullName']
        companySize = i['companySize']
        education = i['education']
        positionName = i['positionName']
        salary = i['salary']
        workYear = i['workYear']
        with open('python.csv', 'a+', encoding='utf-8')as f:
            f.write(f'{city},{companyFullName},{companySize},{education},{positionName},{salary},{workYear}\n')
        print(f'第{j}条数据成功')
        j += 1


if __name__ == '__main__':
    for i in range(1, 11):
        params = data(i)
        get_data(params)
# ctrl+ d