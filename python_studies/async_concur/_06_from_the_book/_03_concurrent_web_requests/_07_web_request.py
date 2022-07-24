'''
It's possible to use 'wait' instead of 'as_completed' and 'gather'. It has 
the upper hand over both.   

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status_code

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = \
            [asyncio.create_task(fetch_status_code(session, 'https://xzxzxample.com')),
            asyncio.create_task(fetch_status_code(session, 'https://example.com'))]
        done, pending = await asyncio.wait(fetchers) # the ALL_COMPLETED option is default for the 'wait' function. 
                                                     # Therefore, 'wait' won't return until all is done. 
        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')

        for done_task in done: # Even though an exception occured, it will be placed in the 'done' set. 
            result = await done_task
            print(result)
asyncio.run(main())
