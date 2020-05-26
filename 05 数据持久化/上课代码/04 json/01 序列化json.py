import json

# 对象在运行过程中只存在于内容
data = {
    'name': 'ACME',
    'shares': 100,
    'price': 542.23
}

# 列表
data_list = [data, data, data]
# 有顺序就可以根据位置取值

# json序列化 json格式 可以使字符串 可以使列表 可以使字典
# 字典        键值对 可变的 无序的 复杂的 数据类型
# 字符串      有序的 不可变的数据类型
# 把字典转化成字符串
json_str = json.dumps(data)
print(json_str)
print(type(json_str))
json_list_str = json.dumps(data_list)
print(json_list_str)
print(type(json_list_str))

with open('json.csv', mode='w', encoding='utf-8') as f:
    f.write(json_list_str)
