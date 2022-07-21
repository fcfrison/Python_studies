'''
Instead of doing the timeout control manually, as 
we did in  '06_cancelling_tasks.py', it's possible
to enjoy a utility function provided by the asyncio 
library, called wait_for.
'''
import asyncio
from util import delay

async def main():
    delay_task = asyncio.create_task(delay(2))  
    try:
        result = await asyncio.wait_for(delay_task, timeout=1) # here the task starts to run and if the execution time is 
                                                                # greater than the timeout a exception pops up.
        print(result)
    except asyncio.exceptions.TimeoutError:
        print('Got a timeout!')
        print(f'Was the task cancelled? {delay_task.cancelled()}')
asyncio.run(main())