import json
import pprint

with open('json.csv', mode='r', encoding='utf-8') as f:
    text = f.read()
print(type(text))
pprint.pprint(text)
data = json.loads(text)
print(type(data))
pprint.pprint(data)
