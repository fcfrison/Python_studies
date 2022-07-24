import asyncio
from aiohttp import ClientSession
from util import async_timed


@async_timed()
async def fetch_status_code(session: ClientSession, url: str) -> int:
    '''
    Coroutine that takes in a session and a URL and return the status code 
    from the given URL.

    parameters
    --------------------
    session: ClientSession
    url: str

    '''
    async with session.get(url) as result:
        return result.status
        
@async_timed()
async def fetch_status_w_delay( session: ClientSession,
                                url: str,
                                delay:int = 0) -> int:
    '''
    Coroutine that take in a session and a URL, sleeps for a determined amount of time 
    and return the status code from the given URL. 

    parameters
    --------------------
    session: ClientSession
    url: str
    delay: int 
    '''
    await asyncio.sleep(delay)
    async with session.get(url) as result:
        return result.status