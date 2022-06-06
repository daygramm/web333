import asyncio
import threading


async def hello1():
    print("1Hello world! (%s)" % threading.currentThread())
    await asyncio.sleep(1)
    print("1Hello again! (%s)" % threading.currentThread())


async def hello2():
    print("2Hello world! (%s)" % threading.currentThread())
    await asyncio.sleep(1)
    print("2Hello again! (%s)" % threading.currentThread())


loop = asyncio.get_event_loop()
tasks = [hello1(), hello2()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
