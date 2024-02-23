import asyncio


async def sleep():
    await asyncio.sleep(1)


async def task():
    for _ in range(2):
        print("Task")
        print("current loop: ", asyncio.get_event_loop())
        await sleep()


loop = asyncio.get_event_loop()
loop.run_until_complete(task())
