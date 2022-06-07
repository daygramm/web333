import MySQLdb

# 打开数据库连接
db = MySQLdb.connect(
    "coder.53site.com", "admin", "Mangosteen0!", "metabus", charset="utf8"
)

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 创建数据表SQL语句
sql = """SELECT * FROM free_mint_catched"""
cursor.execute(sql)

results = cursor.fetchall()
for row in results:
    print("name: {} \t\t\tminter_contract: {}".format(row[1], row[2]))
