'''
It's possible to use 'wait' instead of 'as_completed' and 'gather'. It has 
the upper hand over both. Besides, it provides us the task.result() and 
task.exception() methods for dealing with the tasks that are done.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
import logging
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status_code

@async_timed()
async def main():
    async with ClientSession() as session:
        good_request = fetch_status_code(session, 'https://www.example.com')
        bad_request = fetch_status_code(session, 'python://bad')
        fetchers = [asyncio.create_task(good_request), # it's good practice to wrap the coroutine 
                    asyncio.create_task(bad_request)]  # in a task.
        done, pending = await asyncio.wait(fetchers) # given that ALL_COMPLETED is default,
                                                     # all the tasks must be completed before 
                                                     # the thread goes on.
        print(f'Done task count: {len(done)}')
        print(f'Pending task count: {len(pending)}')
        for done_task in done:
            if done_task.exception() is None:
                print(f'sucessfull results = {done_task.result()}')
            else:
                logging.error("Request got an exception",
                            exc_info=done_task.exception())
asyncio.get_event_loop().run_until_complete(main())  