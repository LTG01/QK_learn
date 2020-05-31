import numpy
import pytesseract
from PIL import Image, ImageFont, ImageDraw

from fontTools.ttLib import TTFont

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
font_path = '6e317246.woff'

# 打开文件
font = TTFont(font_path)
font.saveXML('大众-字体.xml')
# 获取字体编码（特殊的编码）
code_list = font.getGlyphOrder()[2:]
# 新建一张图片
im = Image.new("RGB", (1800, 1800), (255, 255, 255))
image_draw = ImageDraw.Draw(im)
# 绘制图片中, 显示的字体
font = ImageFont.truetype(font_path, 40)

count = 15
# 将需要转化的内容划分15等份， 否则会绘制在一行
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
# # 去除空白及换行
result_str = result.replace(" ", "").replace("\n", "")
# 将内容替换成网页的格式，准备去网页中进行替换
print(code_list)
html_code_list = [i.replace("uni", "&#x") + ";" for i in code_list]
print(html_code_list)
map_dict = dict(zip(html_code_list, list(result_str)))
print(map_dict)
