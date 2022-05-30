from web3 import Web3

infura_url = "https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

print(web3.eth.blockNumber)

balance = web3.eth.getBalance("0xac7208065DF757968e92AEBAd4eF95Bf2b1BD3aC")
print(web3.fromWei(balance, "ether"))
