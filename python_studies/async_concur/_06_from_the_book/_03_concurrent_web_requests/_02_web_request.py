'''
It's possible to make requests via asynchronous processing.

The code below was created by Matthew Fowler in the book 'Python 
Concurrency with asyncio-Manning Publications (2022)'. 
'''
import asyncio
import aiohttp
from aiohttp import ClientSession # ClientSession basically creates a session.
from util import async_timed


@async_timed()
async def fetch_status(session: ClientSession, url: str) -> int:
    '''
    Coroutine that take in a session and a URL and return the status code 
    for the given URL
    '''
    async with session.get(url) as result:  # here, we use the session to run a GET HTTP
                                            # request against the URL.
        return result.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session: # session points to an object of the class ClientSession
        url = 'https://www.example.com'
        status = await fetch_status(session, url)
        print(f'Status for {url} was {status}')

asyncio.get_event_loop().run_until_complete(main())