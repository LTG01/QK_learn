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

sql = 'select * from python;'
cursor.execute(sql)
# cursor.fetchall() 获取所有的查询结果
# cursor.fetchone() 获取所有的查询结果
# for i in cursor.fetchall():
#     print(i)
print(cursor.fetchone())
print(cursor.fetchmany(10))
# 保存提交
conn.commit()
cursor.close()
conn.close()
