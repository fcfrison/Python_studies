'''
It's possible also to cancel a task (for instance, if it takes 
too long to complete).
'''
import asyncio
from asyncio import CancelledError
from util import delay


async def main():
    long_task = asyncio.create_task(delay(10)) # instantiating a task.
    seconds_elapsed = 0
    while not long_task.done():
        print('Task not finished, checking again in a second.')
        print(f'iteration number {seconds_elapsed}')
        await asyncio.sleep(1) # here is the point where the task starts to run.
                                # it's also in this point that the CancelledError is raised.
        seconds_elapsed +=  1
        if seconds_elapsed == 5: # timeout manual control
            long_task.cancel() 
    try:
        await long_task
    except CancelledError:
        print('Our task was cancelled')


asyncio.run(main())