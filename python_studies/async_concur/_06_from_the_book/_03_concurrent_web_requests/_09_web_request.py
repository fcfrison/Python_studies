'''
One of the parameters of the wait method is 'return_when=asyncio.FIRST_EXCEPTION'.
In this case, if an exception occurs, then 'wait' will return. 

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
import logging
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status_w_delay

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = \
            [asyncio.create_task(fetch_status_w_delay(session, 
                                'python://bad.com')),
            asyncio.create_task(fetch_status_w_delay(session, 
                                'https://www.example.com', delay=3)),
            asyncio.create_task(fetch_status_w_delay(session, 
                                'https://www.example.com', delay=3))]
        done, pending = await asyncio.wait(fetchers,
                                    return_when=asyncio.FIRST_EXCEPTION)
        print(f'Done task count: {len(done)}') # Once an exception occurs, 'wait' returns.
        print(f'Pending task count: {len(pending)}')
        for done_task in done: # all the done tasks are filtered here.
            if done_task.exception() is None:
                print(done_task.result())
            else:
                logging.error("Request got an exception",
                        exc_info=done_task.exception())
        for pending_task in pending:
            pending_task.cancel() # pending tasks are cancelled
asyncio.run(main())