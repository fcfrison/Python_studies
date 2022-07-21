'''
It's possible, instead of doing nothing while waiting for the 
sleep time passes, to do something (like print stuff on the screen).
'''

import asyncio
from util import delay
async def hello_every_second():
    for i in range(2):
        await asyncio.sleep(1)
        print(f'I am running other code while I am waiting!(i={i})')
async def main():
    first_delay = asyncio.create_task(delay(3))
    second_delay = asyncio.create_task(delay(3))
    await hello_every_second() # here, all tasks start to run.
    await first_delay
    await second_delay

asyncio.run(main())