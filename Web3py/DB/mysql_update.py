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

# update 
sql = """
	UPDATE productnotes 
    SET note_text='Update Note',
        note_date=%s
    WHERE prod_id='Test'
	"""
try:
    cursor.execute(sql,datetime.datetime.now())
    db.commit()  # 提交到数据库执行，一定要记提交哦
    print("update success")
except Exception as e:
    db.rollback()  # 发生错误时回滚
    print(e)

# release
cursor.close()
db.close()
