'''
The code bellow presents a concurrency that behaves the way we 
expected: multiple task executing at the same time (or at least it seems!!!)
'''

import asyncio
from util import delay
async def main():
    sleep_for_three = asyncio.create_task(delay(3)) # creating a task
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))
    await sleep_for_three # in this point, all tasks start to run.
    await sleep_again
    await sleep_once_more
asyncio.run(main())