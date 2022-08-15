import asyncio
import logging
from aiohttp import ClientSession
from util import async_timed
from extract import fetch_status_w_delay

@async_timed()
async def main():
    async with ClientSession() as session:
        url = 'https://www.example.com'
        url_1 = 'https:example.com'
        pending = [ asyncio.create_task(fetch_status_w_delay(session, url)),
                    asyncio.create_task(fetch_status_w_delay(session, url_1,1)),
                    asyncio.create_task(fetch_status_w_delay(session, url,2))]
        print(pending)
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