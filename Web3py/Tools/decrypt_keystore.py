import json
from web3 import Web3

infura_url = "https://rinkeby.infura.io/v3/1649bfcc28344a1cb472a4b7640f72c0"
web3 = Web3(Web3.HTTPProvider(infura_url))

print(web3.isConnected())

keystore = json.loads(
    '{"address": "2578f31ce3f8f45e10f9688dde2b8294243dd50a", "crypto": {"cipher": "aes-128-ctr", "cipherparams": {"iv": "2685f77a3f5e0266b2c0d7f265232955"}, "ciphertext": "91a9fb8b3363045def4e187bc20ab9cf7bf717e56a5bd6d0b9feb8b6f8c2fee2", "kdf": "scrypt", "kdfparams": {"dklen": 32, "n": 262144, "r": 1, "p": 8, "salt": "fa3858c042ec24fb35f63ebe9d4953b6"}, "mac": "b122dd71a5b1a8f6783c64178b76af3cc77ced96c0946c4d26a7ae4624c827d0"}, "id": "3a30d5ae-75b1-4c23-88d7-21f25c902cd1", "version": 3}'
)

privateKey = web3.eth.account.decrypt(keystore, "password")
print(privateKey.hex())
