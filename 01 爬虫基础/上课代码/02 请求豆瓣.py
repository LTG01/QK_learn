import requests

# 加上User-Agent之后还是请求不到数据
# header 参数是一个字典
headers = {
    'Host': 'movie.douban.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}

response = requests.get('https://movie.douban.com/top250', headers=headers)

print(response.text)
print(response.request.headers)
