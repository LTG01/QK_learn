"""
采集地址：https://www.ximalaya.com/youshengshu/16411402/
目标：前三页的所有音频
"""
import requests
headers = {
    'referer': 'https://www.ximalaya.com/youshengshu/16411402/',
    'origin': 'https://www.ximalaya.com',
    'authority': 'www.ximalaya.com',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36',
}


def get_one_mp3(songid):
    # 改变id就能得到新的音频下载地址
    response = requests.get('https://www.ximalaya.com/revision/play/v1/audio?id='+songid+'&ptype=1', headers=headers)

    dict_data = response.json()
    # print(dict_data)
    mp3_url = dict_data['data']['src']

    print(mp3_url)

get_one_mp3('98936430')
