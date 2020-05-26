import requests
import parsel


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

chapter_url = 'http://www.shuquge.com/txt/8659/index.html'

response = requests.get(url=chapter_url, headers=headers)

response.encoding = response.apparent_encoding
html = response.text

selector = parsel.Selector(html)
print(selector)
print('-'*50)
# 二次提取
dd_a = selector.css('.listmain dd a')
for a in dd_a:
    # getall 提取很多个，返回列表
    # get 提取一个，返回字符串
    print(a.css("a::text").get())
    print(a.css("a::attr(href)").get())
