import json
from eth_typing import Address
from web3 import Web3

infura_url = "https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())


abi = json.loads(
    '[{"inputs":[],"name":"addNumber","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"getNumber","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"uint256","name":"num","type":"uint256"}],"name":"setNumber","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
)
address = "0xFC23F3AfE3d60Bf10c39247BA0Cc5b1bB8c8c6A6"

contract = web3.eth.contract(address=address, abi=abi)

num = contract.functions.getNumber().call()

print("number:{} ", num)
