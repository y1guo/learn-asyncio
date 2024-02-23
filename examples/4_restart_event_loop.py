import asyncio
import time


def trampoline(name: str = ""):
    print(name, end=" ")
    print(time.time())
    loop.call_later(0.5, trampoline, name)


loop = asyncio.get_event_loop()
loop.call_soon(trampoline)
loop.call_later(5, loop.stop)
loop.run_forever()

time.sleep(3)
loop.call_later(5, loop.stop)
loop.run_forever()
