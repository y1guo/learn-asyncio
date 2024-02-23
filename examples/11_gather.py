import asyncio
import time


async def keep_printing(message: str):
    while True:
        print(f"{message} {time.time()}")
        try:
            await asyncio.sleep(0.5)
        except asyncio.CancelledError:
            print(f"{message} is cancelled!")
            return


async def async_main():
    coro1 = keep_printing("First")
    coro2 = keep_printing("Second")
    try:
        await asyncio.wait_for(asyncio.gather(coro1, coro2), 5)
    except asyncio.TimeoutError:
        print("Timeout!")


asyncio.run(async_main())
