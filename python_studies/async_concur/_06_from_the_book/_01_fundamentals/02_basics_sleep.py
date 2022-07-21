'''
The method 'sleep' can emulate a long run process. 
'''
import asyncio
import datetime

async def hello_world_message() -> str:
    print(datetime.datetime.now())
    await asyncio.sleep(5)
    return 'Hello World!'

async def main() -> None:
    message = await hello_world_message()
    print(message)

asyncio.run(main())