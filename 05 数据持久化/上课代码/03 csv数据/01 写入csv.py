import csv

# csv 是一种数据格式 excel也是一种数据格式
# csv 默认情况下用逗号分隔数据
ll = [[1, 2, 3, 4],
      [1, 2, 3, 4],
      [5, 6, 7, 8],
      [5, 6, 7, 8]]

# newline='' 每次写入之后，行位结束符是什么
with open('example1.csv', 'w', newline='') as csv_file:
    # csv_write csv写入对象
    csv_write = csv.writer(csv_file)
    for l in ll:
        csv_write.writerow(l)
        # csv_file.write(",".join(['1', '2', '3']))
        # csv_file.write('\n')
