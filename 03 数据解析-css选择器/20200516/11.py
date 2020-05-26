import pymysql

# 连接数据库


db = pymysql.connect(    host='localhost',
    port=3306,
    user='root',
    passwd='1qazxsw23edc',
    db='db_ltg',
    charset='utf8')
# 获取游标
cursor = db.cursor()
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
#
# # 创建数据表SQL语句
# sql = """CREATE TABLE EMPLOYEE (
#          FIRST_NAME  CHAR(20) NOT NULL,
#          LAST_NAME  CHAR(20),
#          AGE INT,
#          SEX CHAR(1),
#          INCOME FLOAT )"""
#
# cursor.execute(sql)

sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac1', 'Mohan', 20, 'M', 2000)"""
try:
    cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except:
    # 发生错误时回滚
    db.rollback()





sql = "SELECT * FROM EMPLOYEE WHERE INCOME > {}".format(200)
try:
    # 执行SQL语句
    cursor.execute(sql)
    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print("fname={},lname={},age={},sex={},income={}".format(fname, lname, age, sex, income))

except:
    print("Error: unable to fecth data")