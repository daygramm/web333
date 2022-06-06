# from rediscluster import RedisCluster

# redis_client = RedisCluster(
#     startup_nodes=[
#         {"host": "172.21.157.3", "port": 27000},
#         {"host": "172.21.157.4", "port": 27000},
#         {"host": "172.21.157.5", "port": 27000}
#     ],
#     # password='LA1954b!',
#     socket_connect_timeout=5,
#     socket_timeout=5,
#     skip_full_coverage_check=True,
#     max_connections=50
# )
import redis
from redis.sentinel import Sentinel


class RedisClient():
    def __init__(self, db=0, env='local'):
        if env == 'prod':
            # 连接哨兵服务器(主机名也可以用域名)
            sentinel = Sentinel([('172.21.157.3', 27000), ('172.21.157.4', 27000), ('172.21.157.5', 27000)], socket_timeout=3)
            self.master = sentinel.master_for('mymaster', socket_timeout=3, db=db, decode_responses=True)
            self.slave = sentinel.slave_for('mymaster', socket_timeout=3, db=db, decode_responses=True)
        elif env == 'local' or env == 'test':
            self.master = redis.Redis(host='112.124.15.145', port=6379, decode_responses=True, db=db, password='LA1954b!')
            self.slave = redis.Redis(host='112.124.15.145', port=6379, decode_responses=True, db=db, password='LA1954b!')
