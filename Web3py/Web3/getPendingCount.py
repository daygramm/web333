import asyncio
import threading
import json
import pymysql
from bxcommon.rpc.provider.ws_provider import WsProvider
from flask import Flask, jsonify, request
from web3 import Web3

import redis_client
import requests

_evn = "test"
redis = redis_client.RedisClient(db=2, env=_evn)

db = pymysql.connect(
    host="coder.53site.com", user="admin", password="Mangosteen0!", database="metabus"
)
# db = pymysql.connect(
#     host="172.21.157.7", user="magister_jvm", password="Mangosteen0!", database="metabus"
# )
cursor = db.cursor()

web3_wss = Web3(
    Web3.HTTPProvider("https://mainnet.infura.io/v3/23e4a77870ea4deab047bb6911a28144")
)

app = Flask(__name__, instance_path="/{project_folder_abs_path}/instance")
contracts = []

# 获取所有要查询pending的合约地址
def get_all_contracts():
    sql = """SELECT * FROM free_mint_catched"""
    cursor.execute(sql)

    results = cursor.fetchall()
    contracts = []
    for row in results:
        contracts.append(row[2])
    return contracts


# 每小时更新一次合约地址
async def update_contracts():
    global contracts
    while True:
        contracts = get_all_contracts()
        print("update contract: {}".format(str(contracts)))
        await asyncio.sleep(3600)


# 订阅所有pending交易
async def subscribe_pending():
    async with WsProvider(
        uri="wss://api.blxrbdn.com/ws",
        headers={
            "Authorization": "MWZjMTEzZWMtODI1NS00ZmZiLTgyNmMtMWZkMThmOGZmNjVkOjAzNTljYmViYjQ3MWE1MjY4NDZjMmI2MTJlYmNkYjk4"
        },
    ) as ws:
        subscription_id = await ws.subscribe(
            "pendingTxs",
            {
                "include": ["tx_hash", "tx_contents"],
                "filters": "to in " + str(contracts),
            },
        )

        while True:
            try:
                next_notification = await ws.get_next_subscription_notification_by_id(
                    subscription_id
                )
                txHash = next_notification.notification["txHash"]
                contract = next_notification.notification["txContents"]["to"]
                redis.master.rpush(str(contract).lower(), txHash)
                print("new pending for contract:{} txhash:{}".format(contract, txHash))
                pass
            except Exception as e:
                print(e)
        await ws.unsubscribe(subscription_id)


# 检查已有的pending交易 移除已经完成的交易
async def check_txs_status():
    while True:
        try:
            for contract in contracts:
                contract_key = str(contract).lower()
                tx_hashs = redis.slave.lrange(contract_key, 0, -1)
                for tx_hash in tx_hashs:
                    # 获取pending状态 result为空时pending
                    etherscan_req = "https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash={}&apikey=FRDHJP4ZBMH3X7R45XBAIWD23NPGQMD2TP".format(
                        tx_hash
                    )
                    tx_status = json.loads(requests.get(etherscan_req).text)
                    if tx_status["result"] != None:  # result 不为空时脱离pending状态
                        redis.master.lrem(contract_key, 1, tx_hash)
                        # print("脱离pending状态: {}".format(tx_hash))

                print(
                    "\npending txs count: {} contract:{} ".format(
                        redis.slave.llen(contract_key), contract_key
                    )
                )

        except Exception as e:
            print(e)
        await asyncio.sleep(3)


def app_run():
    app.run(host="0.0.0.0", port=9923)


@app.route("/metabus/api/pyextra/pending_count", methods=["GET"])
def get_pending_count():
    try:
        contract = request.args.get("contract")
        pending_count = redis.slave.llen(contract)
        return (
            jsonify({"msg": "success", "data": {"pending_count": pending_count}}),
            200,
        )
    except Exception as e:
        return jsonify({"msg": e}), 500


if __name__ == "__main__":
    contracts = get_all_contracts()
    # print(str(contracts))

    # Flask
    app_run_thread = threading.Thread(target=app_run)
    app_run_thread.start()

    # pending
    loop = asyncio.get_event_loop()
    tasks = [check_txs_status(), subscribe_pending(), update_contracts()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
