import requests

url = 'https://www.guazi.com/cs/08f1a29d96e51324x.htm'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
    # 'Cookie': 'uuid=56bf67a9-6601-4f73-a498-5f4cfe4a0094; antipas=Q1I7IZ3001367926L096075; track_id=79308092267462656; cityDomain=cs; clueSourceCode=%2A%2300; user_city_id=204; ganji_uuid=4935535954726485946313; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; sessionid=c0ea9366-7dd1-4f63-d475-5d58ed80e763; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%2279308092267462656%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2256bf67a9-6601-4f73-a498-5f4cfe4a0094%22%2C%22ca_city%22%3A%22cs%22%2C%22sessionid%22%3A%22c0ea9366-7dd1-4f63-d475-5d58ed80e763%22%7D; close_finance_popup=2020-05-21; lng_lat=112.832025_28.247595; gps_type=1; preTime=%7B%22last%22%3A1590063731%2C%22this%22%3A1590063722%2C%22pre%22%3A1590063722%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A73336717671%7D'
}

cookies = {
    'Cookie': 'uuid=56bf67a9-6601-4f73-a498-5f4cfe4a0094; antipas=Q1I7IZ3001367926L096075; track_id=79308092267462656; cityDomain=cs; clueSourceCode=%2A%2300; user_city_id=204; ganji_uuid=4935535954726485946313; guazitrackersessioncadata=%7B%22ca_kw%22%3A%22-%22%7D; sessionid=c0ea9366-7dd1-4f63-d475-5d58ed80e763; lg=1; cainfo=%7B%22ca_a%22%3A%22-%22%2C%22ca_b%22%3A%22-%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22pcbiaoti%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%22-%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22track_id%22%3A%2279308092267462656%22%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%2256bf67a9-6601-4f73-a498-5f4cfe4a0094%22%2C%22ca_city%22%3A%22cs%22%2C%22sessionid%22%3A%22c0ea9366-7dd1-4f63-d475-5d58ed80e763%22%7D; close_finance_popup=2020-05-21; lng_lat=112.832025_28.247595; gps_type=1; preTime=%7B%22last%22%3A1590063731%2C%22this%22%3A1590063722%2C%22pre%22%3A1590063722%7D; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A73336717671%7D'
}

# 有些时候,直接复制的 cookie 是不能使用的
response = requests.get(url, headers=headers, cookies=cookies)
print(response)
response.encoding = response.apparent_encoding
print(response.text)
"""
response: 服务器返回过来的数据

request: 客户端(chrome) 发送给服务器的数据
"""