import os
from dotenv import load_dotenv

def get(key):
    load_dotenv("../config/.env")
    if os.getenv("MODE") == "dev":
        load_dotenv("../config/.env.dev")

    elif os.getenv("MODE") == "prod":
        load_dotenv("../config/.env.prod")

    else:
        load_dotenv("../config/.env.local")

    return os.getenv(key)


def dev(key):
    load_dotenv("../config/.env.dev")
    return os.getenv(key)


def prod(key):
    load_dotenv("../config/.env.prod")
    return os.getenv(key)


def local(key):
    load_dotenv("../config/.env.local")
    return os.getenv(key)

