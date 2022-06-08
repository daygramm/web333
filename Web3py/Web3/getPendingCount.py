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
redis = redis_client.RedisClient(db=0, env=_evn)

db = pymysql.connect(
    host="47.114.151.253", user="admin", password="Mangosteen0!", database="metabus"
)
# db = pymysql.connect(
#     host="172.21.157.7", user="magister_jvm", password="Mangosteen0!", database="metabus"
# )
cursor = db.cursor()
web3_url = "https://mainnet.infura.io/v3/23e4a77870ea4deab047bb6911a28144"
web3_wss = Web3( Web3.HTTPProvider(web3_url))
web3 = Web3(Web3.HTTPProvider(web3_url))
erc721_abi = json.loads(
    '[{"inputs":[],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[],"name":"ApprovalCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"ApprovalQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"ApprovalToCurrentOwner","type":"error"},{"inputs":[],"name":"ApproveToCaller","type":"error"},{"inputs":[],"name":"BalanceQueryForZeroAddress","type":"error"},{"inputs":[],"name":"MintToZeroAddress","type":"error"},{"inputs":[],"name":"MintZeroQuantity","type":"error"},{"inputs":[],"name":"OwnerQueryForNonexistentToken","type":"error"},{"inputs":[],"name":"TransferCallerNotOwnerNorApproved","type":"error"},{"inputs":[],"name":"TransferFromIncorrectOwner","type":"error"},{"inputs":[],"name":"TransferToNonERC721ReceiverImplementer","type":"error"},{"inputs":[],"name":"TransferToZeroAddress","type":"error"},{"inputs":[],"name":"URIQueryForNonexistentToken","type":"error"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"approved","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"owner","type":"address"},{"indexed":true,"internalType":"address","name":"operator","type":"address"},{"indexed":false,"internalType":"bool","name":"approved","type":"bool"}],"name":"ApprovalForAll","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"previousOwner","type":"address"},{"indexed":true,"internalType":"address","name":"newOwner","type":"address"}],"name":"OwnershipTransferred","type":"event"},{"anonymous":false,"inputs":[{"indexed":true,"internalType":"address","name":"from","type":"address"},{"indexed":true,"internalType":"address","name":"to","type":"address"},{"indexed":true,"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"Transfer","type":"event"},{"inputs":[{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"approve","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"flipSale","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"getApproved","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"owner","type":"address"},{"internalType":"address","name":"operator","type":"address"}],"name":"isApprovedForAll","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxFreePerWallet","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxPerTx","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"maxSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"count","type":"uint256"}],"name":"mint","outputs":[],"stateMutability":"payable","type":"function"},{"inputs":[],"name":"mintEnabled","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"owner","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"price","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"renounceOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"},{"internalType":"bytes","name":"_data","type":"bytes"}],"name":"safeTransferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"operator","type":"address"},{"internalType":"bool","name":"approved","type":"bool"}],"name":"setApprovalForAll","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"string","name":"uri","type":"string"}],"name":"setBaseURI","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"amount","type":"uint256"}],"name":"setFreeAmount","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"uint256","name":"_newPrice","type":"uint256"}],"name":"setPrice","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"bytes4","name":"interfaceId","type":"bytes4"}],"name":"supportsInterface","outputs":[{"internalType":"bool","name":"","type":"bool"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"tokenURI","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalFree","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"address","name":"from","type":"address"},{"internalType":"address","name":"to","type":"address"},{"internalType":"uint256","name":"tokenId","type":"uint256"}],"name":"transferFrom","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[{"internalType":"address","name":"newOwner","type":"address"}],"name":"transferOwnership","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"withdraw","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
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


def send_dingtalk(text):
    headers = {'Content-Type': 'application/json; charset=UTF-8'}
    url = 'https://oapi.dingtalk.com/robot/send?access_token=0e1bcb4ca5583283e0070ac47a0ec9da62fba2aadd7edecf9e5f593fb77c2854'    
    data = {
        "msgtype": "markdown",
        "markdown": {
            "title": "NFT数量监控",
            "text": text
        }
    }
    print(requests.post(url, headers=headers, data=json.dumps(data)))

def get_supply(contracts):
    i = 0
    l = len(contracts)
    logT = []
    logS = []
    for c in contracts:
        address = Web3.toChecksumAddress(c)
        contract = web3.eth.contract(address=address, abi=erc721_abi)
        
        try:                    
            totalSupply = contract.functions.totalSupply().call()
            key = str(c).lower()+'_total_supply'
            redis.master.set(key, totalSupply)
            print("{}/{}.totalSupply: {}".format(i,l,redis.slave.get(key)))
        except Exception as e:
            # print("合约: {} 找不到 totolSupply 对应的函数, Exception: {}".format(c,e))
            logT.append("- 合约: {} 找不到 totolSupply 对应的函数, Exception: {}\n".format(c,e))

        try:
            maxSupply = contract.functions.maxSupply().call()
            key = str(c).lower()+'_max_supply'
            redis.master.set(key, maxSupply)
            print("{}/{}.maxSupply: {}".format(i,l,redis.slave.get(key)))
        except Exception as e:
            # print("合约: {} 找不到 maxSupply 对应的函数, Exception: {}".format(c,e))
            logS.append("- 合约: {} 找不到 maxSupply 对应的函数, Exception: {}\n".format(c,e))

        i = i + 1
    msgT = "### totalSupply:\n{}".format(''.join(logT)) 
    msgS = "### maxSupply:\n{}".format(''.join(logS))
    print(msgT)
    print(msgS)
    # send_dingtalk(msgT + "\n" + msgS)

# 每小时更新一次合约地址
async def update_contracts():
    global contracts
    while True:
        contracts = get_all_contracts()
        # print("update contract: {}".format(str(contracts)))
        get_supply(contracts)
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
                    # etherscan_req = "https://api.etherscan.io/api?module=proxy&action=eth_getTransactionReceipt&txhash={}&apikey=FRDHJP4ZBMH3X7R45XBAIWD23NPGQMD2TP".format(
                    #     tx_hash
                    # )
                    # tx_status = json.loads(requests.get(etherscan_req).text)
                    print("\npending txs count: {} contract: {} txhash: {}".format(redis.slave.llen(contract_key), contract_key, tx_hash))
                    try:
                        web3.eth.getTransactionReceipt(tx_hash)
                        redis.master.lrem(contract_key, 1, tx_hash)
                        print("\npending txs remove count: {} contract:{} ".format(redis.slave.llen(contract_key), contract_key))
                    except Exception as e:
                        pass
                
            # get_supply(contracts)
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
    # address = sys.argv[1]
    address = "0xaC9Bb427953aC7FDDC562ADcA86CF42D988047Fd"
    contracts.append(address)

    # Flask
    app_run_thread = threading.Thread(target=app_run)
    app_run_thread.start()

    # pending
    loop = asyncio.get_event_loop()
    tasks = [check_txs_status(), subscribe_pending(), update_contracts()]
    loop.run_until_complete(asyncio.wait(tasks))
    loop.close()
