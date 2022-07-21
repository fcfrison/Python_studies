'''
There are two ways for handling exceptions with gather:
1) return_exceptions=False
    In this case, if any of our coroutines throws an exception, 
    our gather call will also throw that exception when we await it.
2) return_exceptions=True
    In this case, gather will return any exceptions as part of the 
    result list it returns when we await it.

In the example presented here, we're going to show the second handling.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''
import asyncio
from aiohttp import ClientSession
from chapter_04 import fetch_status_code
from util import async_timed

@async_timed()
async def main():
    async with ClientSession() as session: # session points to an object of the class ClientSession
        urls = ['https://example.com', 'python:/ / example .com']
        tasks = [fetch_status_code(session, url) for url in urls]   # Generate a list of coroutines for
                                                                    # each request we want to make
        results = await asyncio.gather(*tasks, return_exceptions=True) # create the tasks and start the requests.
        exceptions = [res for res in results if isinstance(res, Exception)] # filter the exceptions
        successful_results = [res for res in results if not isinstance(res, Exception)] # filter the valid results
    print(f'All results: {results}')
    print(f'Finished successfully: {successful_results}')
    print(f'Threw exceptions: {exceptions}')
asyncio.get_event_loop().run_until_complete(main())
