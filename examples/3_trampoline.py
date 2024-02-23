import asyncio
import time


def trampoline(name: str = ""):
    print(name, end=" ")
    print(time.time())
    loop.call_later(0.5, trampoline, name)


loop = asyncio.get_event_loop()
loop.call_soon(trampoline, "First")
loop.call_soon(trampoline, "Second")
loop.call_soon(trampoline, "Third")
loop.call_later(5, loop.stop)
loop.run_forever()
