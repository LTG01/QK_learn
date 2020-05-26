import json

# json 序列化过程中，默认会把中文转化为unicode吗
data = {
    'name': '青灯',
    'shares': 100,
    'price': 542.23
}

json_str = json.dumps(data, ensure_ascii=False)
print(json_str)

# 反序列化，再序列化
