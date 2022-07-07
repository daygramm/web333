import pymysql

# 打开数据库连接
db = pymysql.connect(
    host="192.168.1.172",
    user="root",
    password="love1115",
    database="mysql"
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 创建数据表SQL语句
sql = """SELECT * FROM user"""
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
    print("name: {} \t\t\tminter_contract: {}".format(row[1], row[2]))
