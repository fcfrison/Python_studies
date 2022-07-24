'''
One of the parameters of the wait method is 'return_when=asyncio.FIRST_COMPLETED'.
In this case, if an event occurs (being it a sucess or an exception), then 'wait' 
will return. 

In the code below, once a exception is raised, all the pending task are cancelled.

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
        url = 'https://www.example.com'
        url_1 = 'https:example.com'
        pending = [ asyncio.create_task(fetch_status_w_delay(session, url)),
                    asyncio.create_task(fetch_status_w_delay(session, url_1,1)),
                    asyncio.create_task(fetch_status_w_delay(session, url,2))]
        while pending: # while pending task, continue.
            done, pending = await asyncio.wait(pending,
                                    return_when=asyncio.FIRST_COMPLETED)
            print(f'Done task count: {len(done)}')
            print(f'Pending task count: {len(pending)}')
            for done_task in done:
                if done_task.exception() is None:
                    print(done_task.result())
                else:
                    logging.error("Request got an exception",
                    exc_info=done_task.exception())
                    for pending_task in pending: # if an error occurs, the cancel the remaining tasks.
                        pending_task.cancel()
                        pending = False

asyncio.run(main())