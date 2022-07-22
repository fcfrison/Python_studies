'''
The function as_completed presents a parameter for timeout control.
One of the drawbacks with timeouts and asyncio.as_completed is that
tasks created will still be running in the background.

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
        for finished_task in asyncio.as_completed(fetchers,timeout=2): # controlling for timeout
            try:
                result = await finished_task
                print(result)
            except asyncio.TimeoutError:
                print('We got a timeout error!')
        
        for task in asyncio.tasks.all_tasks():# shows all the pending tasks
            print(task)

asyncio.get_event_loop().run_until_complete(main())    

