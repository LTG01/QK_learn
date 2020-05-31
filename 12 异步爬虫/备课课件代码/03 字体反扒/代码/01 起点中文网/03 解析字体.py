# 把字体文件读取为python能理解的对象
from fontTools.ttLib import TTFont

# 映射规则是不变了
eng_2_num = {
    'period': ".", 'two': '2', 'zero': '0', 'five': '5', 'nine': "9", 'seven': '7', 'one': '1', 'three': '3',
    'six': '6', 'four': '4', 'eight': '8'
}


font_name = 'pbrRoZFn.woff'

base_font = TTFont(font_name)
base_font.saveXML('font.xml')
# 获取映射规则
map_list = base_font.getBestCmap()
# 字符编码：字符内容
print(map_list)


# 将英文内容替换成中文内容
for key in map_list.keys():
    map_list[key] = eng_2_num[map_list[key]]

print(map_list)
