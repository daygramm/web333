import json
from eth_typing import Address
from web3 import Web3

ganache_url = "HTTP://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

account1 = "0x5717e031b88C60550F171C6336e11B97B6ACC836"
private_key = "52236ee51c71507d767677eb13151d91324d88962d1037e6e41be6a4cde1061a"
account2 = "0x4ea38e9Bd20810755C4a9b41843845B405dB2e03"

print(web3.isConnected())

abi = json.loads(
    """[
    {
      "inputs": [],
      "stateMutability": "nonpayable",
      "type": "constructor"
    },
    {
      "inputs": [],
      "name": "name",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [],
      "name": "owner",
      "outputs": [
        {
          "internalType": "address",
          "name": "",
          "type": "address"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [],
      "name": "symbol",
      "outputs": [
        {
          "internalType": "string",
          "name": "",
          "type": "string"
        }
      ],
      "stateMutability": "view",
      "type": "function",
      "constant": true
    },
    {
      "inputs": [],
      "name": "totalSupply",
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
      "inputs": [
        {
          "internalType": "address",
          "name": "to",
          "type": "address"
        },
        {
          "internalType": "uint256",
          "name": "amount",
          "type": "uint256"
        }
      ],
      "name": "transfer",
      "outputs": [],
      "stateMutability": "nonpayable",
      "type": "function"
    },
    {
      "inputs": [
        {
          "internalType": "address",
          "name": "account",
          "type": "address"
        }
      ],
      "name": "balanceOf",
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
    }
  ]"""
)
address = "0xa5Ea73992B43d4462a52f97d9ef047E3fFD141e4"
contract = web3.eth.contract(address=address, abi=abi)

symbol = contract.functions.symbol().call()
print(symbol)

totalSupply = contract.functions.totalSupply().call()
print(web3.fromWei(totalSupply, "ether"))

num = contract.functions.balanceOf("0x5717e031b88C60550F171C6336e11B97B6ACC836").call()
print("number:{} ", num)

# get the nonce
nonce = web3.eth.getTransactionCount(account1)
# build transaction
tx = {
    "nonce": nonce,
    "to": account2,
    "value": web3.toWei(1, "ether"),
    "gas": 2000000,
    "gasPrice": web3.toWei("50", "gwei"),
}
# sign transaction
signed_tx = web3.eth.account.signTransaction(tx, private_key)
# send transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)
# get transaction hash
print(web3.toHex(tx_hash))
