import asyncio
import threading


async def hello1():
    while True:
        print("hello1 (%s) *************************************" % threading.currentThread())   
        await asyncio.sleep(3)

async def hello2():
    while True:
        print("hello2 (%s)" % threading.currentThread())
        await asyncio.sleep(1)

loop = asyncio.get_event_loop()
tasks = [hello1(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
