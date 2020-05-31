import re

import pytesseract
import requests
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont
import numpy

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36',
    'Referer': 'http://www.dianping.com/changsha/ch10/r12149',
    'Cookie': '_lxsdk_cuid=1704ff33901c8-0fc6f4bb8331ae-366b420b-7e9000-1704ff33901c8; _lxsdk=1704ff33901c8-0fc6f4bb8331ae-366b420b-7e9000-1704ff33901c8; _hc.v=b04f69fc-3c80-4008-5839-bf96c74c7572.1581889305; dplet=a9800db2dfb4c48994773498927732b6; dper=3a3c23b40e1f6ddc6aa0d31ab68de7c4c64e8968e260752b18380fadb969c536601ff8ebe9f432b765555fc9d8f7c11810ccda14e579f0bd721376f0361a78a1df715dcc09b3effac0af278c0af2f60aaef65401f5243049d669413beeb744fc; ua=%E5%BF%99%E7%A2%8C%E7%9A%84%E8%BA%AF%E4%BD%93; ctu=c4cbf7c8dc53a7adc479157bd67df302d8cf2cd7afdb00064575dd4b5a28b72f; ll=7fd06e815b796be3df069dec7836c3df; cy=344; cye=changsha; s_ViewType=10; _lxsdk_s=170533f8fdf-e8b-0cc-5fc%7C%7C178'
}


def get_response(url):
    response = requests.get(url, headers=headers)
    return response


def get_font(html):
    """下载字体"""
    # 下载css，获取字体的下载地址
    css_url = re.findall(
        'type="text/css" href="(//s3plus.sankuai.com/v1/mss_0a06a471f9514fc79c981b5466f56b91/svgtextcss/.*?.css)"',
        html)
    print(css_url)
    css_response = get_response('https:' + css_url[0])
    print(css_response.text)
    # 取css文件里面匹配字体的下载链接
    font_url = re.findall(
        '@font-face{font-family: "PingFangSC-Regular-review";src.*?format.*?url\("(.*?)"\);}',
        css_response.text)
    print(font_url)
    font_name = font_url[0].split('/')[-1]
    font_response = get_response('https:' + font_url[0])
    with open(font_name, mode='wb') as f:
        f.write(font_response.content)
    return font_name


def font_convert(font_path):  # 将web下载的字体文件解析，返回其编码和汉字的对应关系
    font = TTFont(font_path)  # 打开文件
    # 字体编码（特殊的编码）
    code_list = font.getGlyphOrder()[2:]
    # 新建一张图片
    im = Image.new("RGB", (1800, 1800), (255, 255, 255))
    # print(im)
    image_draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, 40)

    count = 15
    # 将需要转化的内容划分15等份
    # 等分
    array_list = numpy.array_split(code_list, count)

    for i in range(len(array_list)):
        # print('替换之前的', array_list[i])
        # 讲js的unicode码转化为python的unicode
        new_list = [i.replace("uni", "\\u") for i in array_list[i]]
        # print('替换之后的', new_list)
        # 将列表变为字符串
        text = "".join(new_list)
        # print('列表变字符串', text)
        # encode decode
        # 把文字变成二进制
        # 将字符串进行反向编码
        text = text.encode('utf-8').decode('unicode_escape')
        # print('反向编码之后的', text)
        # 将文件绘制到图片
        # 指定字体进行绘制
        image_draw.text((0, 100 * i), text, font=font, fill="#000000")

    im.save("sss.jpg")
    im.show()
    im = Image.open("sss.jpg")  # 可以将图片保存到本地，以便于手动打开图片查看
    result = pytesseract.image_to_string(im, lang="chi_sim")
    print(result)
    # # 去除空白及换行
    result_str = result.replace(" ", "").replace("\n", "")
    # 将内容替换成网页的格式，准备去网页中进行替换
    print(code_list)
    html_code_list = [i.replace("uni", "&#x") + ";" for i in code_list]
    print(html_code_list)
    # print(len(html_code_list))
    # print(len(result_str))
    return dict(zip(html_code_list, list(result_str)))


if __name__ == '__main__':
    # 1. 获取网页
    html = get_response('http://www.dianping.com/shop/22314796').text
    with open('替换之前的.html', mode='w', encoding='utf-8') as f:
        f.write(html)
    # 2. 获取字体
    font_name = get_font(html)
    # 3. 获取字体映射的规则 alt+enter
    font_rule_map = font_convert(font_name)
    print(font_rule_map)

"""

开发速度

运行速度

"""