import redis_client
from web3 import Web3

_evn = "test"
redis = redis_client.RedisClient(db=2, env=_evn)

if __name__ == "__main__":

    # 列表操作
    redis.master.rpush("test_list", 1, 2, 3)

    list_len = redis.slave.llen("test_list")
    print("列表长度:{}".format(list_len))

    list_test = redis.slave.lrange("test_list",0,-1)
    print("列表:{}".format(list_test))
    
    redis.master.delete("test_list")

    # 散列表
    # redis.master.hset("test_hash_table", "key", "value")
    # print(redis.slave.hget("test_hash_table", "key"))
    # redis.master.delete("test_hash_table")
