import csv

with open('names.csv', 'r', newline="", encoding='utf-8') as f:
    """
        newline="" 防止每次写入之后多出一个换行符
    """
    csv_dict_read = csv.DictReader(f)
    for item in csv_dict_read:
        print(item['first_name'], item['last_name'])
        print(item, item['last_name'])
