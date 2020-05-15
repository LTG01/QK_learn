"""
作业提交格式
    + 使用源代码的方式提交，题目用 `注释` 的方式写在源代码里面。
    + 作业文件命名：第几次作业-编号-作业编号-姓名.py（例如01-00-01-正心.py）
      自己的编号到这个文档中查找：【腾讯文档】作业提交表https://docs.qq.com/sheet/DU01wRUNRb1B5S1l6?c=H46A0BI0
    + 作业提交格式为 第几次作业-编号-姓名.zip(发送两个作业的压缩包)
      例如正心的第一次作业提交文件为 01-00-正心.zip
    + 提交到QQ邮箱：2328074219@qq.com
    + 作业在第二天上课前讲解，不会的提前半个小时到课堂
    + 写作业时自己先思考如何完成，当作业讲解之后还是不会做时，再来问老师。

将上课的案例-爬取小说完善。爬取《剑来》所有章节用章节名分别保存。
"""
"""清下下方开始编写代码"""
import requests
import re

# 下载一本，需要下载很多章


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

# 1. 先提取目录页面
index_response = requests.get('http://www.shuquge.com/txt/8659/index.html', headers=headers)
index_response.encoding = index_response.apparent_encoding
index_html = index_response.text
# print(index_html)

results = re.findall('<dd><a href="(.*?)">(.*?)</a></dd>', index_html, re.S)
print(results)
for url, name in results[12:]:
    print('http://www.shuquge.com/txt/8659/'+url, name)

    chapter_name = name + '.txt'
    chapter_url = 'http://www.shuquge.com/txt/8659/'+url

    response = requests.get(url=chapter_url, headers=headers)

    response.encoding = response.apparent_encoding
    html = response.text

    result = re.findall('<div id="content" class="showtxt">(.*?)</div>', html, re.S)
    # 如果有内容，就进行下载
    if result:
        with open(chapter_name, mode='w', encoding='utf-8') as f:
            f.write(result[0].replace('<br/>', '').replace('&nbsp;', ""))
