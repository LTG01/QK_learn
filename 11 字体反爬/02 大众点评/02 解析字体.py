"""
分析字体->找到css文件->html


获取不到映射规则, 不可能手动去进行修改

机器能不能获取这个规则

把字体内容全部绘制出来



"""
import numpy
import pytesseract
from PIL import Image, ImageFont, ImageDraw

from fontTools.ttLib import TTFont

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
font_path = '788c62d4.woff'

# 打开文件
font = TTFont(font_path)
# 获取字体编码（特殊的编码）
code_list = font.getGlyphOrder()[2:]
print(code_list)
"""逆向部分,将特殊字体绘制到一张图片上去"""
# 新建一张图片
im = Image.new("RGB", (1800, 1800), (255, 255, 255))
# 绘制图片的对象
image_draw = ImageDraw.Draw(im)
# 绘制图片中, 显示的字体
font = ImageFont.truetype(font_path, 40)

count = 15
# 将特殊编码等分为15分
array_list = numpy.array_split(code_list, count)

for i in range(len(array_list)):
    # print('替换之前的', array_list[i])
    # 将js的unicode码转化为python的unicode
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

# im.save("sss.jpg")  # 可以将图片保存到本地，以便于手动打开图片查看
# im.show()
result = pytesseract.image_to_string(im, lang="chi_sim")
print(result)
# # # 去除空白及换行
result_str = result.replace(" ", "").replace("\n", "")
# 将内容替换成网页的格式，准备去网页中进行替换
print(code_list)
html_code_list = [i.replace("uni", "&#x") + ";" for i in code_list]
print(html_code_list)
print(result_str)
# 将特殊编码与识别的字体一一兑现
map_dict = dict(zip(html_code_list, list(result_str)))
print(map_dict)

with open('替换之前.html', mode='r', encoding='utf-8') as f:
    text = f.read()

for key, value in map_dict.items():
    print(key, value)
    text = text.replace(key, value)

with open('替换之后.html', mode='w', encoding='utf-8') as f:
    f.write(text)
