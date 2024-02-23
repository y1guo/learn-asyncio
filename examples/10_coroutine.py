import asyncio
import time


async def print3times():
    for _ in range(3):
        print(time.time())
        await asyncio.sleep(0.1)


coro1 = print3times()
coro2 = print3times()
print(type(print3times))
print(type(coro1))
print(type(coro2))
asyncio.run(coro1)
time.sleep(1)
asyncio.run(coro2)
time.sleep(1)

# can't run the same coroutine twice
asyncio.run(coro1)
