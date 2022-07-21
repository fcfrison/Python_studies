'''
The code bellow presents a concurrency that behaves like a 
sequential code. No task are created.
'''
import asyncio
from util import *


async def add_one(number: int) -> int:
    print('add_one_coroutine')
    return number + 1

async def hello_world_message() -> str:
    print('hello_world_message_coroutine')
    await delay(1)
    return 'return of the coroutine hello_world_message: Hello World!'

async def main() -> None:
    message = await hello_world_message()
    one_plus_one = await add_one(1)
    print(one_plus_one)
    print(message)

asyncio.run(main())