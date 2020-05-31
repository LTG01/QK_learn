from fontTools.ttLib import TTFont

map_str_2_number = {
    'period': '.',
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9
}

# 专门用于读取字体
# 1. 视同 ttfont 读取字体
base_font = TTFont('qgnjJmsk.woff')
# 2. 把字体文件保存为 xml 格式
base_font.saveXML('font.xml')

map_order = base_font.getGlyphOrder()
print(map_order)
# 获取字体的映射规则(特殊字符->应该显示的字符)
map_list = base_font.getBestCmap()
print(map_list)

# 构建一个可以替换的规则
for key in map_list.keys():
    # map_list[key] 取到'period', 然后对'period'重新赋值
    # map_str_2_number['period'] 取到.
    map_list[key] = map_str_2_number[map_list[key]]

print(map_list)
