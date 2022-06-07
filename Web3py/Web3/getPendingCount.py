import asyncio
import threading
import sys
import json

from bxcommon.rpc.provider.ws_provider import WsProvider
from flask import Flask, jsonify, request
from web3 import Web3

import redis_client
import requests

_evn = "test"
pending_key = "pending_tx_list"
redis = redis_client.RedisClient(db=2, env=_evn)

web3_wss = Web3(
    Web3.HTTPProvider("https://mainnet.infura.io/v3/23e4a77870ea4deab047bb6911a28144")
)

app = Flask(__name__, instance_path="/{project_folder_abs_path}/instance")


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
                "filters": "to = " + address,
            },
        )

        while True:
            try:
                next_notification = await ws.get_next_subscription_notification_by_id(
                    subscription_id
                )
                txHash = next_notification.notification["txHash"]
                # tx_hashs.append(txHash)
                redis.master.rpush(pending_key, txHash)
                pass
            except Exception as e:
                print(e)
        await ws.unsubscribe(subscription_id)


async def check_txs_status():
    while True:
        try:
            tx_hashs = redis.slave.lrange(pending_key, 0, -1)
            for tx_hash in tx_hashs:
                # 获取pending状态 result为空时pending
                etherscan_req = "https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash={}&apikey=FRDHJP4ZBMH3X7R45XBAIWD23NPGQMD2TP".format(
                    tx_hash
                )
                tx_status = json.loads(requests.get(etherscan_req).text)
                if tx_status["result"] != None:  # result 不为空时脱离pending状态
                    redis.master.lrem(pending_key, 1, tx_hash)
                    print("脱离pending状态: {}".format(tx_hash))

            print("\npending txs count: {}".format(redis.slave.llen(pending_key)))

        except Exception as e:
            print(e)
        await asyncio.sleep(3)


def app_run():
    app.run(host="0.0.0.0", port=9988)


if __name__ == "__main__":
    # address = sys.argv[1]
    address = "0x83C8F28c26bF6aaca652Df1DbBE0e1b56F8baBa2"

    # Flask
    app_run_thread = threading.Thread(target=app_run)
    app_run_thread.start()

    # pending
    loop = asyncio.get_event_loop()
    tasks = [check_txs_status(), subscribe_pending()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
