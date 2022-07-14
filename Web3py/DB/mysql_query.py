import pymysql

# init db and cursor
db = pymysql.connect(
	host="192.168.1.172",
	user="gaojian",
	password="password",
	database="mysql_crash_course"
)
cursor = db.cursor()  

# query 
sql = """
	SELECT order_num,cust_id 
	FROM orders
	WHERE order_num > 20006
	"""
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
	print(f"name: {row[0]} \t minter_contract: {row[1]}")

# release
cursor.close()
db.close()