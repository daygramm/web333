import os
from dotenv import load_dotenv

load_dotenv("../config/.env")

print(os.getenv("MODE"))
if os.getenv("MODE") == "dev":
    print("开发环境")
    load_dotenv("../config/.env.dev")
    print(os.getenv("NAME"))

elif os.getenv("MODE") == "prod":
    print("生产环境")
    load_dotenv("../config/.env.prod")
    print(os.getenv("NAME"))
    
else:
    print("本地环境")
    load_dotenv("../config/.env.local")
    print(os.getenv("NAME"))
