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


from copyheaders import headers_raw_to_dict
import csv
import time
import random


def get_agent():
    user_agent = [
        "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:38.0) Gecko/20100101 Firefox/38.0",
        "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 3.0.30729; .NET CLR 3.5.30729; InfoPath.3; rv:11.0) like Gecko",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)",
        "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)",
        "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
        "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; en) Presto/2.8.131 Version/11.11",
        "Opera/9.80 (Windows NT 6.1; U; en) Presto/2.8.131 Version/11.11",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; TencentTraveler 4.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; The World)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SE 2.X MetaSr 1.0; SE 2.X MetaSr 1.0; .NET CLR 2.0.50727; SE 2.X MetaSr 1.0)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser)",
        "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)",
        "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",
        "Mozilla/5.0 (Linux; U; Android 2.3.7; en-us; Nexus One Build/FRF91) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
        "Opera/9.80 (Android 2.3.4; Linux; Opera Mobi/build-1107180945; U; en-GB) Presto/2.8.149 Version/11.10",
        "Mozilla/5.0 (Linux; U; Android 3.0; en-us; Xoom Build/HRI39) AppleWebKit/534.13 (KHTML, like Gecko) Version/4.0 Safari/534.13",
        "Mozilla/5.0 (BlackBerry; U; BlackBerry 9800; en) AppleWebKit/534.1+ (KHTML, like Gecko) Version/6.0.0.337 Mobile Safari/534.1+",
        "Mozilla/5.0 (hp-tablet; Linux; hpwOS/3.0.0; U; en-US) AppleWebKit/534.6 (KHTML, like Gecko) wOSBrowser/233.70 Safari/534.6 TouchPad/1.0",
        "Mozilla/5.0 (SymbianOS/9.4; Series60/5.0 NokiaN97-1/20.0.019; Profile/MIDP-2.1 Configuration/CLDC-1.1) AppleWebKit/525 (KHTML, like Gecko) BrowserNG/7.1.18124",
        "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; HTC; Titan)",
        "UCWEB7.0.2.37/28/999",
        "NOKIA5700/ UCWEB7.0.2.37/28/999",
        "Openwave/ UCWEB7.0.2.37/28/999",
        "Mozilla/4.0 (compatible; MSIE 6.0; ) Opera/UCWEB7.0.2.37/28/999",
        # iPhone 6：
        "Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25",

    ]

    return random.choice(user_agent)




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
    print(cookies)
    # print()
    return cookies



#    cookie: user_trace_token=20200516121447-c75fbdf8-972b-11ea-8008-52540063a8d7; JSESSIONID=ABAAABAABEIABCIF8F30AB92BD8C36409F467165E78830B; SEARCH_ID=876d63a621c14196ae02f5ee3953f6de; X_HTTP_TOKEN=7010a50404777a364942069851c3134a76ac758990; WEBTJ-ID=20200516121454-1721bb1293be49-0359cf206c046e-30677c00-1296000-1721bb1293c835

def get_info_list(page=1):
    headers = {
   'referer': 'https://www.lagou.com/jobs/list_python/p-city_0?',
    'user-agent': get_agent()
}


    info_list=[]
    info_list.append(['城市','公司名','公司规模','学历','职位名称','薪资','工作时间'])
    cookies = get_cookies()
    for i in range(1,page+1):
        url = 'https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false'
        data = {
            "first": "true",
            "pn": str(i),
            "kd": "python"
        }

        time.sleep(random.randint(0,5))

        if i%5==0 :
            cookies = get_cookies()

        response = requests.post(url,data=data,headers=headers,cookies=cookies)
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
    infolist = get_info_list(page=10)
    #
    save_info(infolist)
    pass




