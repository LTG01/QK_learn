import requests
import pprint

url = 'https://image.so.com/j'


def get_params(page):
    # 定义一个方法
    params = {
        "q": "风景",
        "pd": "1",
        "pn": "60",
        "correct": "风景",
        "adstar": "0",
        "tab": "all",
        "sid": "b4383580f831123119cc03535d9ae7c0",
        "ras": "0",
        "cn": "0",
        "gn": "0",
        "kn": "0",
        "crn": "0",
        "bxn": "0",
        "src": "srp",
        "color": "orange",
        "sn": page,
        # "ps": "59",
        # "pc": "59",
    }
    return params


# ctrl + / 注释，取消注释
# alt + 鼠标左键 多选
# print(get_params(60))
# print(get_params(120))
# print(get_params(180))
for page in range(60, 181, 60):
    # 可读性
    params = get_params(page)
    # print(params)
    response = requests.get(url, params=params)
    # 文本内容
    # print(response.text)
    # content 是二进制的内容
    # print(response.content.decode(response.encoding))
    # print(response.url)
    # ctrl+鼠标滚轮
    # 把字符串编程字典
    # 如果不是 json 字符串，调用 .json() 方法就会报错
    # 是字典格式就不会报错，如果不是字典就会报错
    # json 是数据交换格式
    data = response.json()
    # pprint.pprint(response.json())

    """
    下载图片
    """
    images_item = data['list']
    for item in images_item:
        # pprint.pprint(item)
        image_url = item['thumb']
        print(image_url)
