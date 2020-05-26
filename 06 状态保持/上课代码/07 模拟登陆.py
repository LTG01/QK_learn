import requests
import parsel

session = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
}
# 请求github,获取最开始的cookie
session.get('https://github.com/', headers=headers)

# print(response.text)


# 请求登录页面
response = session.get('https://github.com/login')
sel = parsel.Selector(response.text)
timestamp_secret = sel.css('input[name="timestamp_secret"]::attr(value)').get()
print(timestamp_secret)
authenticity_token = sel.css('input[name="authenticity_token"]::attr(value)').get()
print(authenticity_token)


data = {
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'timestamp_secret': timestamp_secret,
    'login': 'pyxxponly@gmail.com',
    'password': 'xxponly1'
}


# # 登录
# logon_url = 'https://github.com/session'
# session.post(url=logon_url, data=data)

# 登录之后的请求效果
setting_response = session.get('https://github.com/settings/profile')

with open('profile_no_login.html', mode='wb') as f:
    f.write(setting_response.content)

# selenium
# session

