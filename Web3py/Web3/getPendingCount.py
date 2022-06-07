import asyncio
import threading
import sys

from bxcommon.rpc.provider.ws_provider import WsProvider
from flask import Flask, jsonify, request
from web3 import Web3


web3_wss = Web3(
    Web3.HTTPProvider("https://mainnet.infura.io/v3/23e4a77870ea4deab047bb6911a28144")
)

app = Flask(__name__, instance_path="/{project_folder_abs_path}/instance")

tx_hashs = []


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
    address = sys.argv[1]

    # Flask
    app_run_thread = threading.Thread(target=app_run)
    app_run_thread.start()

    # pending
    loop = asyncio.get_event_loop()
    tasks = [check_txs_status(), subscribe_pending()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
