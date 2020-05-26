import requests
import parsel


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

chapter_url = 'http://www.shuquge.com/txt/8659/31165742.html'

response = requests.get(url=chapter_url, headers=headers)

response.encoding = response.apparent_encoding
html = response.text

selector = parsel.Selector(html)
h1 = selector.css('h1::text').getall()
print(h1)
# 同一个标签的组合选择器之间不要有空格
content = selector.css('div#content.showtxt::text').getall()
list_content = []
for c in content:
    list_content.append(c.strip())
    print(c.strip())
print(",".join(list_content))