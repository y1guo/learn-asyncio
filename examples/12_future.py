import asyncio


fut = asyncio.Future()
print("fut.done() =", fut.done())
print("fut.cancelled() =", fut.cancelled())
print("Setting result...")
fut.set_result("Hello, Future!")
print("fut.done() =", fut.done())
print("fut.cancelled() =", fut.cancelled())
print("fut.result() =", fut.result())
print("fut.exception() =", fut.exception())
