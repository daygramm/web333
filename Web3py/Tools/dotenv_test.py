import os
from dotenv import load_dotenv

load_dotenv()

if os.getenv("MODE") == "dev":
    print("开发模式")
elif os.getenv("MODE") == "test":
    print("测试模式")
else:
    print("生产模式")
