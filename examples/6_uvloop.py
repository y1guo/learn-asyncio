import asyncio
import uvloop


uvloop.install()
loop = asyncio.get_event_loop()
print(loop)
