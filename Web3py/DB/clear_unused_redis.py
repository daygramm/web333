import pymysql
import redis_client

_evn = "test"
redis = redis_client.RedisClient(db=0, env=_evn)

db = pymysql.connect(
    host="47.114.151.253", user="admin", password="Mangosteen0!", database="metabus"
)
# db = pymysql.connect(
#     host="172.21.157.7",
#     user="magister_jvm",
#     password="Mangosteen0!",
#     database="metabus",
# )
cursor = db.cursor()

# 清除无用的 redis key
def claer_contracts_key():
    sql = """SELECT * FROM free_mint_catched"""
    cursor.execute(sql)

    results = cursor.fetchall()
    for row in results:
        key = str(row[2]).lower()
        maxKey = key + "_max_supply"
        totalKey = key + "_total_supply"
        redis.master.delete(key)
        redis.master.delete(maxKey)
        redis.master.delete(totalKey)
        print("移除redis key: {}  max: {} total: {}".format(key, maxKey, totalKey))


if __name__ == "__main__":
    claer_contracts_key()
