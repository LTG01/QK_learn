import requests
import parsel

headers = {
    "authority": "www.ximalaya.com",
    "path": "/youshengshu/16411402/",
    "referer": "https://www.ximalaya.com/",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36",
}


def get_one_mp3(songid):
    # 改变id就能得到新的音频下载地址
    response = requests.get('https://www.ximalaya.com/revision/play/v1/audio?id=' + songid + '&ptype=1',
                            headers=headers)
    dict_data = response.json()
    # print(dict_data)
    mp3_url = dict_data['data']['src']

    return mp3_url


def download_one_page(page):
    """
    每一个函数都是一个独立的功能
    尽量不要在函数里面调用另外一个函数
    """
    response = requests.get('https://www.ximalaya.com/youshengshu/16411402/p{}'.format(page), headers=headers)
    # print(response.text)
    selector = parsel.Selector(response.text)
    lis = selector.css('li._Vc')
    print(lis)
    # pycharm 的 terminal 里面可以保证结果是对的
    # 浏览器可以让我们看清楚html结构
    results = []
    for li in lis:
        a = li.css('.text._Vc a')
        name = a.css('a::attr(title)').get()
        url = a.css('a::attr(href)').get()
        song_id = url.split('/')[-1]
        # print(song_id, name)
        results.append([song_id, name])
    return results


def save(url, name):
    response = requests.get(url)
    suffix = "." + url.split('.')[-1]
    with open('music\\'+name + suffix, mode='wb') as f:
        f.write(response.content)


# 不容易理解
for page in range(1, 4):
    results = download_one_page(page)
    for song_id, name in results:
        mp3_url = get_one_mp3(song_id)
        # 函数位置参数
        print(mp3_url, name)
        save(mp3_url, name)
