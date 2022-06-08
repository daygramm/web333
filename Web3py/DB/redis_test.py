import redis_client
from web3 import Web3

_evn = "test"
redis = redis_client.RedisClient(db=0, env=_evn)

if __name__ == "__main__":

    # 字符串
    # redis.master.set("test_string_key","test_string_value")
    # redis.master.set("test_int",666)

    # string_value = redis.slave.get("test_string_key")
    # int_value = redis.slave.get("test_int")
    # print(string_value)
    # print(int_value)

    # redis.master.delete("test_string_key")
    # redis.master.delete("test_int")

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
    # redis.master.rpush("test_list", 1, 2, 3)

    # list_len = redis.slave.llen("test_list")
    # print("列表长度:{}".format(list_len))

    # list_test = redis.slave.lrange("0x982a5a3F6ABFD179B3f7649af37942235a90935f", 0, -1)
    # print("列表:{}".format(list_test))

    # print("增:{}".format(redis.master.rpush("test_list", 6)))
    # print("删:{}".format(redis.master.lrem("test_list", 1, 3)))
    # print("\t遍历列表:{}".format(redis.slave.lrange("test_list", 0, -1)))
    # print("改:{}".format(redis.master.lset("test_list", 2, 3)))
    # print("\t遍历列表:{}".format(redis.slave.lrange("test_list", 0, -1)))
    # print("查:{}".format(redis.master.lindex("test_list", 2)))

    # redis.master.delete("test_list")

    
    # print("增:{}".format(redis.master.rpush("eCD3449c707280a812CdE19149C247e1E18611d8", "0x558e4d3880573c2692da2ed938f5929d6c94ce80c3c317159bd70697eaaddb30")))
    # list_test = redis.slave.lrange("eCD3449c707280a812CdE19149C247e1E18611d8", 0, -1)
    # print("列表:{}".format(list_test))


    string_value = redis.slave.get("eCD3449c707280a812CdE19149C247e1E18611d8".lower()+"_total_supply")
    int_value = redis.slave.get("eCD3449c707280a812CdE19149C247e1E18611d8_max_supply")
    print(string_value)
    print(int_value)

    # redis.master.delete("pending_tx_list") 
    # redis.master.delete("0x982a5a3F6ABFD179B3f7649af37942235a90935f")
