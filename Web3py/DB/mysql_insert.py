import pymysql
import datetime

db = pymysql.connect(
    host="192.168.1.172",
    user="gaojian",
    password="password",
    charset="utf8",
    database="mysql_crash_course",
)
cursor = db.cursor()

sql = """insert into productnotes(prod_id, note_date, note_text) values(%s,%s,%s)"""  # 注意此处与前一种形式的不同

try:
    cursor.execute(sql, ("Test", datetime.datetime.now(), "Test Note"))
    db.commit()  # 提交到数据库执行，一定要记提交哦
except Exception as e:
    db.rollback()  # 发生错误时回滚
    print(e)