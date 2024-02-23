import asyncio


async def example(count: int):
    print(f"[{count}] in example")
    print(f"[{count}] before first await")
    await asyncio.sleep(0)
    print(f"[{count}] after first await")
    if count == 0:
        return "result"
    for i in range(count):
        print(f"[{count}, {i}] before second await")
        await asyncio.sleep(1)
        print(f"[{count}, {i}] after second await")
    print(f"[{count}] before third await")
    return await example(count - 1)


asyncio.run(example(3))