'''
One of the methods provided by aiohttp for running awaitables concurrently is 
asyncio.gather.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''

import asyncio
from aiohttp import ClientSession
from chapter_04 import fetch_status_code
from util import async_timed

@async_timed()
async def main():
    async with ClientSession() as session:
        urls = ['https://example.com' for _ in range(500)] # creates a list with 1000 urls.
        '''
        status_codes = [await fetch_status_code(session, url) for url in urls] # this code executes things synchronously
        '''
        requests = [fetch_status_code(session, url) for url in urls] # Generate a list of coroutines for
                                                                    # each request we want to make
        status_codes = await asyncio.gather(*requests) # Wait for all requests to complete
        
        
        print(status_codes)
asyncio.get_event_loop().run_until_complete(main())