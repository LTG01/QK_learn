import csv

dict_list = [{'first_name': 'Baked', 'last_name': 'Beans'},
             {'first_name': 'Lovely'},
             {'first_name': 'Wonderful', 'last_name': 'Spam'}]


with open('names.csv', 'w', newline="", encoding='utf-8') as f:
    """
        newline="" 防止每次写入之后多出一个换行符
    """
    # 键有什么作用（键不能少，数据里面的字典可以少）
    fieldnames = ['first_name', 'last_name']

    csv_dict_write = csv.DictWriter(f, fieldnames=fieldnames)
    # 写入文件头
    csv_dict_write.writeheader()
    for item in dict_list:
        csv_dict_write.writerow(item)
