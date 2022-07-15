from web3 import Web3

infura_url = "https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"
web3test = Web3(Web3.HTTPProvider(infura_url))
# get variable name
print(f"{web3test=}".split('=')[0])
print(web3test.isConnected())

print(web3test.eth.blockNumber)

balance = web3test.eth.getBalance("0xac7208065DF757968e92AEBAd4eF95Bf2b1BD3aC")
print(web3test.fromWei(balance, "ether"))

