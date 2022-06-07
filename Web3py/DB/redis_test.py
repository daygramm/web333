import redis_client
from web3 import Web3

_evn = "test"
redis = redis_client.RedisClient(db=2, env=_evn)

if __name__ == "__main__":

    # 字符串
    # redis.master.set("test_string_key","test_string_value")

    # string_value = redis.slave.get("test_string_key")
    # print(string_value)

    # redis.master.delete("test_string_key")

    # 列表操作
    # redis.master.rpush("test_list", 1, 2, 3)

    # list_len = redis.slave.llen("test_list")
    # print("列表长度:{}".format(list_len))

    # list_test = redis.slave.lrange("test_list",0,-1)
    # print("列表:{}".format(list_test))

    # redis.master.delete("test_list")

    # 散列表
    # redis.master.hset("test_hash_table", "key", "value")
    # print(redis.slave.hget("test_hash_table", "key"))
    # redis.master.delete("test_hash_table")

    # 列表的增删改查
    redis.master.rpush("test_list", 1, 2, 3)

    list_len = redis.slave.llen("test_list")
    print("列表长度:{}".format(list_len))

    list_test = redis.slave.lrange("test_list", 0, -1)
    print("列表:{}".format(list_test))

    print("增:{}".format(redis.master.rpush("test_list", 6)))
    print("删:{}".format(redis.master.lrem("test_list", 1, 3)))
    print("\t遍历列表:{}".format(redis.slave.lrange("test_list", 0, -1)))
    print("改:{}".format(redis.master.lset("test_list", 2, 3)))
    print("\t遍历列表:{}".format(redis.slave.lrange("test_list", 0, -1)))
    print("查:{}".format(redis.master.lindex("test_list", 2)))

    redis.master.delete("test_list")
