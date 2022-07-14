import pymysql

# 初始化数据库连接, 获取cursor
db = pymysql.connect(
	host="192.168.1.172",
	user="gaojian",
	password="password",
	database="mysql_crash_course"
)
cursor = db.cursor()  

# 查询数据库
sql = """SELECT order_num,cust_id FROM orders"""
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
	print(f"name: {row[0]} \t\t\t minter_contract: {row[1]}")

# 释放数据库连接
cursor.close()
db.close()