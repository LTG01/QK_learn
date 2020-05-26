# -*- coding: utf-8 -*-
import os
import re
import openpyxl

wb = openpyxl.Workbook()
sheet = wb.active
# 把文件夹下面的文件名全部列出来
filename = os.listdir('作业提交')
print(filename)

for file in filename:
    result = re.match('(\d{1,2})-(\d{1,3})', file)
    col = int(result.group(1))
    row = int(result.group(2))
    print(col, row)
    sheet.cell(row=row, column=col).value = 1

wb.save('作业统计.xlsx')