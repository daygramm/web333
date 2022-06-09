import pymongo

mongo = pymongo.MongoClient(
    "mongodb://112.124.15.145:27117/"
)
collection = mongo.eth_fullchain_dev.eth_transaction_obj_dev

result = collection.find_one(
    {"hash": "0xf27b5aaf3ccaf761dbc756766359c87cb874611c054b9268934ace71af90aef5"}
)

if __name__ == "__main__":
    print(type(result))
    print(result)
