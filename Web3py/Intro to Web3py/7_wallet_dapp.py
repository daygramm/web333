import json
from eth_typing import Address
from web3 import Web3

infura_url = "https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

acccount = web3.eth.account.create()
print(acccount)
print("address:\t%s"%acccount.address)
print("private key:\t%s"%acccount.privateKey.hex())
print("keystore:\t%s",acccount.encrypt("password"))
