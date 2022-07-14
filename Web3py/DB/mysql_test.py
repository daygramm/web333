import pymysql
import datetime

# init db and cursor
db = pymysql.connect(
	host="192.168.1.172",
	user="gaojian",
	password="password",
	database="mysql_crash_course"
)
cursor = db.cursor()  

# insert 
sql = """
	INSERT INTO productnotes(prod_id, note_date, note_text) 
	VALUES(%s,%s,%s)
	"""
values = ("Test", datetime.datetime.now(), "Test Note")
try:
    cursor.execute(sql, values)
    db.commit()  # 提交到数据库执行，一定要记提交哦
    print("insert success")
except Exception as e:
    db.rollback()  # 发生错误时回滚
    print(e)

# release
cursor.close()
db.close()
