import requests

headers = {
    'origin': 'https://www.lagou.com',
    'referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
    'authority': 'www.lagou.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}
response = requests.get("https://www.lagou.com/jobs/list_python/p-city_3?px=default", headers=headers)

# 把一个 cookiejar 对象变成字典

print(response.cookies.get_dict())

# cookies 是一个字典，cookie是一个键值对

# cookies 包含了很多个cookie，一个cookie是一个键值对

cookies = {'X_HTTP_TOKEN': '42daf4b72327b2816090559851bf5e71415983ed09',
           'user_trace_token': '20200515215506-b4da41ad-c988-442f-9d33-e1712d66d737',
           'JSESSIONID': 'ABAAAECAAEBABII6CDF2D641BFF8993DC92F76C8EB35F6D',
           'SEARCH_ID': '337d41a4a7d747869bf55ed31a797ebc'}

# ctrl + alt + l

print(response.cookies)
print(type(response.cookies))

# ctrl + z 撤销修改

# tab or 回车