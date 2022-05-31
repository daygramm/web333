import json
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"
web3 = Web3(Web3.HTTPProvider(infura_url))

isConnected = web3.isConnected()
print("Blockchain Connect Status: {}".format(isConnected))

# Etherscan.io 上的数据都可以获得, 可用于爬虫和数据监控
blockNumber = web3.eth.blockNumber
print("Blcok Number: {}".format(blockNumber))

block = web3.eth.getBlock(blockNumber)
print(web3.toJSON(block))

hash = "0x298e673d583c943e498d886ab1d9189b4e4904f3d839b86b619d0877fb7e112e"
transaction = web3.eth.getTransactionByBlock(hash, 1)
print(web3.toJSON(transaction))
