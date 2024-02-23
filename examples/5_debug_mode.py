import asyncio


async def sleep():
    await asyncio.sleep(1)


async def task():
    for _ in range(10):
        print("Task")
        print("current loop: ", asyncio.get_event_loop())
        await sleep()


def hog():
    res = 0
    for i in range(10_000):
        for j in range(10_000):
            res += i * j
    return res


loop = asyncio.get_event_loop()
loop.set_debug(True)
loop.call_later(5, hog)
loop.run_until_complete(task())
