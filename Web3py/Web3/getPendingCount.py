import asyncio
import json
import threading
import time

import requests
from bxcommon.rpc.provider.ws_provider import WsProvider
from flask import Flask, jsonify, request

# from bloxroute_cli.provider.cloud_wss_provider import CloudWssProvider
from web3 import Web3


web3_wss = Web3(
    Web3.HTTPProvider("https://mainnet.infura.io/v3/23e4a77870ea4deab047bb6911a28144")
)


# opensea_get_contract_slug_url = "https://api.opensea.io/api/v1/asset_contract/%s"
# opensea_apikey = 'a813d22b142c4a5a83952b797fb7e98a'
app = Flask(__name__, instance_path="/{project_folder_abs_path}/instance")

# opensea_api_headers = {
#     "Accept": "application/json",
#     "X-API-KEY": opensea_apikey
# }
tx_hashs = []
tx_infos = []


# @app.route("/bloxroute/txInfo", methods=["POST"])
# def insert_tx_info():
#     """
#     加入各种信息
#         :return:
#     """
#     try:
#         data = request.get_json()
#         dic = {"send_time": time.time(), "data": data}
#         tx_infos.append(dic)
#         return jsonify({"msg": "success"}), 200
#     except Exception as e:
#         logger.log_info("Exception:" + str(e))
#         return jsonify({"msg": e}), 500


# Enterprise customers can use lines 5 - 9
async def subscribe_pending():
    # async with CloudWssProvider(
    #         ssl_dir="../python/external_gateway/registration_only",
    #         ws_uri="wss://eth.feed.blxrbdn.com:28333"  # use wss://bsc.feed.blxrbdn.com:28333 for BSC
    # ) as ws:
    # Non-enterprise cutomers can use lines 11 - 14
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
                "filters": "to in [0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D] and value > 0",
            },
        )

        while True:
            try:
                next_notification = await ws.get_next_subscription_notification_by_id(
                    subscription_id
                )
                txHash = next_notification.notification["txHash"]
                tx_hashs.append(txHash)
                pass
            except Exception as e:
                print(e)
        await ws.unsubscribe(subscription_id)


async def check_txs_status():
    async with WsProvider(
        uri="wss://api.blxrbdn.com/ws",
        headers={
            "Authorization": "MWZjMTEzZWMtODI1NS00ZmZiLTgyNmMtMWZkMThmOGZmNjVkOjAzNTljYmViYjQ3MWE1MjY4NDZjMmI2MTJlYmNkYjk4"
        },
    ) as ws:
        while True:
            try:
                for tx_hash in tx_hashs:
                    # 获取状态
                    pass
                print("\npending txs count: {}".format(len(tx_hashs)))
            except Exception as e:
                print(e)
            await asyncio.sleep(1)
        await ws.unsubscribe(subscription_id)


def app_run():
    app.run(host="0.0.0.0", port=9988)


if __name__ == "__main__":
    # Flask
    app_run_thread = threading.Thread(target=app_run)
    app_run_thread.start()

    # pending
    loop = asyncio.get_event_loop()
    tasks = [check_txs_status(),subscribe_pending()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
