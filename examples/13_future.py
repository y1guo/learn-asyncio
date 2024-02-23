import asyncio
import time


def callback(fut: asyncio.Future):
    print("called by", fut)


loop = asyncio.get_event_loop()
fut = asyncio.Future()
fut.add_done_callback(callback)
fut.add_done_callback(lambda fut: loop.stop())
fut.set_result("Hello, Future!")
print("Results are set!")
time.sleep(5)
print("Starting event loop...")
loop.run_forever()
loop.close()
