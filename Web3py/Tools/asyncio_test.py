import asyncio
import threading


async def hello1():
    while True:
        print(f"hello1 ({threading.currentThread()}) *********************************")
        await asyncio.sleep(3)


async def hello2():
    while True:
        print(f"hello2 ({threading.currentThread()})")
        await asyncio.sleep(1)


tasks = [hello1(), hello2()]

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
