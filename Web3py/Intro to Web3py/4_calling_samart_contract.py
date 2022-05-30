import json
from eth_typing import Address
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))
print(web3.isConnected())

abi = json.loads(
    """[
    {
      "inputs": [
        {
          "internalType": "uint256",
          "name": "num",
          "type": "uint256"
        }
      ],
      "name": "setNumber",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [],
      "name": "getNumber",
      "outputs": [
        {
          "internalType": "uint256",
          "name": "",
          "type": "uint256"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [],
      "name": "addNumber",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    }
  ]"""
)

# web3.py 中所有用到地址的地方，不能直接传入地址，需要用toChecksumAddress()转一下
address = web3.toChecksumAddress("0x7DA89b21fa11b85Eb3f116e35BE584C13BB2104e")
contract = web3.eth.contract(address=address, abi=abi)

symbol = contract.functions.getNumber().call()
print(symbol)

# 'message': 'from not found; is required'
web3.eth.defaultAccount = web3.eth.accounts[0]
contract.functions.setNumber(666).transact()

symbol = contract.functions.getNumber().call()
print(symbol)

tx_hash = contract.functions.addNumber().transact()
# waiting for transaction finish and return
web3.eth.waitForTransactionReceipt(tx_hash)

symbol = contract.functions.getNumber().call()
print(symbol)