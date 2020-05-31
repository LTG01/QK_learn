from fontTools.ttLib import TTFont
import requests
import re

map_rule = {
    'period': '.', 'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'
}


def get_font(html):
    # 获取font相关信息
    font_link = re.findall("format\('eot'\); src: url\('(.*?)'\) format\('woff'\)", html)[0]
    response_woff = requests.get(font_link)
    filename = font_link.split('/')[-1]
    with open(filename, "wb") as f:
        f.write(response_woff.content)
    return filename


def get_map_rule(font_name):
    # 替换所有的加密字符
    base_font = TTFont(font_name)
    base_font.saveXML('font.xml')
    key_list = base_font.getBestCmap()
    for key in key_list:
        key_list[key] = map_rule[key_list[key]]
    return key_list


def get_page(base_url):
    """获取网页数据"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    }
    r = requests.get(base_url, headers=headers)
    # print(r.text)
    return r.text


def replace_html(map_dict, html):
    """返回解密的html文件"""
    for key in map_dict.keys():
        html = html.replace('&#' + str(key) + ';', map_dict[key])
    with open('new_html.html', mode='w', encoding='utf-8') as f:
        f.write(html)


if __name__ == '__main__':
    target_url = 'https://book.qidian.com/info/1010734492'
    html = get_page(target_url)
    # print(html)
    with open('old_html.html', mode='w', encoding='utf-8') as f:
        f.write(html)
    font_name = get_font(html)
    map_rule_dict = get_map_rule(font_name)
    print(map_rule_dict)
    replace_html(map_rule_dict, html)
