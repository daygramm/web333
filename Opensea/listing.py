import os
import sys
import json
import requests

sys.path.append("..")
from utils.logger import Logger

logger = Logger(os.path.basename(__file__)).logger

private_key = "972ff45576a91a46b600be4b2ab7f41545858a1940fa2976172c168fe6d705ae"


def opensea_sell(contract_address, owner_address,owner_key, gas_price=0.003):
    privateKey = 0
    asset_contract_address = contract_address
    token_id_array = [1]
    accountAddress = owner_address
    user_key = owner_key
    price = 0.02 + float(gas_price)
    time = 1

    logger.info(f"############### token_id_array: {token_id_array}")

    opensea_sell_url_test = (
        "http://172.21.157.5:7203/magisterAdminApi/cng/ApprovalForAllAndCreateTest"
    )
    common_headers = {"Content-Type": "application/json; charset=UTF-8"}
    for token_id in token_id_array:
        res = requests.request(
            "POST",
            opensea_sell_url_test,
            headers=common_headers,
            data=json.dumps(
                {
                    "privateKey": privateKey,
                    "asset_contract_address": asset_contract_address,
                    "token_id": token_id,
                    "accountAddress": accountAddress,
                    "user_key": user_key,
                    "price": price,
                    "time": time,
                }
            ),
        )
        logger.info(
            f"###################################### token id: {token_id} sell result: {res.text}"
        )
        res = json.loads(res.text)

        msg_ding = ""
        if res["result"] and res["result"] == "success":
            msg_ding += "### Opensea 上架成功\n"
            msg_ding += "- Private Key Id: {}\n".format(privateKey)
            msg_ding += "- Contract Address: {}\n".format(contract_address)
            msg_ding += "- Token Id: {}\n".format(token_id)
            msg_ding += "- Owner Address: {}\n".format(owner_address)
            msg_ding += "- Price: {}\n".format(price)
            msg_ding += "- Time: {}\n".format(time)
        else:
            msg_ding += "### Opensea 上架失败\n"
            msg_ding += "- Private Key Id: {}\n".format(privateKey)
            msg_ding += "- Contract Address: {}\n".format(contract_address)
            msg_ding += "- Token Id: {}\n".format(token_id)
            msg_ding += "- Owner Address: {}\n".format(owner_address)
            msg_ding += "- Price: {}\n".format(price)
            msg_ding += "- Time: {}\n".format(time)
            msg_ding += "- Msg: {}\n".format(res)

        logger.info(msg_ding)




if __name__ == "__main__":
    nft_address = "0xE040ad7a71f86ED498919ACBCDE1E0C0234B3EdE"
    owner_address = "0xac7208065DF757968e92AEBAd4eF95Bf2b1BD3aC"
    owner_key = "972ff45576a91a46b600be4b2ab7f41545858a1940fa2976172c168fe6d705ae"
    opensea_sell(nft_address,owner_address,owner_key)