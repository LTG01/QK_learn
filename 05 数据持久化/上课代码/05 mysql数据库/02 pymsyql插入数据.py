import csv

import pymysql

# 链接远程服务器
conn = pymysql.connect(
    host='134.175.188.27',  # 服务器的ip
    port=3306,              # 数据库开发的端口
    user='windows',         # 用户名
    password='123456',      # 密码
    database='test',        # 需要使用的数据库
)

# 获取游标(做事的)
cursor = conn.cursor()


with open('python.csv', mode='r', encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    for row in csv_reader:
        print(row)
        # print(conn)
        # pymsyql 是运行 sql 指令工具
        sql = 'insert into python(`name`,`company`,`nember`,`edu`,`position`,`salary`,`experience`) values(%s,%s,%s,%s,%s,%s,%s)'
        cursor.execute(sql, row)
        # break

# 保存提交
conn.commit()
cursor.close()
conn.close()
