import asyncio
import time


def print_time():
    print(time.time())
    time.sleep(1)


loop = asyncio.get_event_loop()
loop.call_soon(print_time)
loop.call_soon(print_time)
loop.run_until_complete(asyncio.sleep(1))
