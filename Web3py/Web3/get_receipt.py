import json
from eth_typing import Address
from web3 import Web3

infura_url = "https://mainnet.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

receipt=web3.eth.getTransactionReceipt("0x497bde1dc39095f459dde21f12742021a39ce7031173b1cb78120d6c1774faa9")
print(receipt)
