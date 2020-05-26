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
import requests
import parsel

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36',
    'Host': 'www.shuquge.com'
}

def get_catalog(catalog_url):
    details_urls = []
    response = requests.get(catalog_url, headers)
    response.encoding = response.apparent_encoding
    s = parsel.Selector(response.text)
    chapter_url_list = s.css('dd a::attr(href)')[12:].getall()
    for chapter_url in chapter_url_list:
        url = 'http://www.shuquge.com/txt/8659/' + chapter_url
        details_urls.append(url)
    return details_urls


def article_parsing(details_urls):
    for details_url in details_urls:
        response = requests.get(details_url, headers=headers)
        response.encoding = response.apparent_encoding
        s = parsel.Selector(response.text)
        title = s.css('h1::text').get()
        content_list = [data.strip() for data in s.css('#content::text').getall()]
        content = '\n'.join(content_list)
        if content:
            print(title)
        else:
            print([title], [content], response.url)

        # save(title, content)


def save(title, content):
    with open(r'.\\剑来\\' + title + '.txt', mode='w', encoding='utf-8') as f:
        print('正在下载：', title)
        f.write(content)


catalog_url = 'http://www.shuquge.com/txt/8659/index.html'
details_urls = get_catalog(catalog_url)
article_parsing(details_urls)
