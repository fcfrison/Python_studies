'''
A drawback with the method 'gather' is that it waits for all
awaitables to finish before allowing access to any results. From 
the efficiency perspective, this can be problematic, considering
that some requests can take a long time to return while others don't.

To handle this kind of situation, asyncio API provides a function
called as_completed. The code presented in this module shows how 
to use the above mentioned function.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
from aiohttp import ClientSession
from util import async_timed
from chapter_04 import fetch_status_w_delay

@async_timed()
async def main():
    async with ClientSession() as session:
        fetchers = [ # creating a list of coroutines. 
            fetch_status_w_delay(session,'https://www.example.com', 1),
            fetch_status_w_delay(session,'https://www.example.com', 2),
            fetch_status_w_delay(session,'https://www.example.com', 10)
            ] 
        for finished_task in asyncio.as_completed(fetchers): # wrapping the coroutines in tasks
            print(await finished_task)

asyncio.get_event_loop().run_until_complete(main())    

        
        
        