from aiohttp import ClientSession
from util import async_timed

@async_timed()
async def fetch_status_code(session: ClientSession, url: str) -> int:
    '''
    Coroutine that take in a session and a URL and return the status code 
    for the given URL
    '''
    async with session.get(url) as result:
        return result.status