import asyncio
import time


async def keep_printing(message: str):
    while True:
        print(f"{message} {time.time()}")
        await asyncio.sleep(0.5)


async def async_main():
    await keep_printing("First")
    await keep_printing("Second")


asyncio.run(async_main())
