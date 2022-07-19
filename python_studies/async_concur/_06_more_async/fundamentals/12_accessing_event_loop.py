'''
Even if the event loop was created through the 'run' function, 
it's possible to access it using the 'get_running_loop'. 
'''
import asyncio
from util import delay

def call_later():
    '''
    This is a regular Python function. 
    '''
    print("I'm being called in the future!")

async def main():
    loop = asyncio.get_running_loop() # accessing the event loop.
    loop.call_soon(call_later) # adding a regular func to the event loop.
    await delay(1)  # calling the delay coroutine inside the event loop.
                    # the call_later is called while the coroutine delay is
                    # sleeping. 
asyncio.run(main()) # starting the event loop, whose management is delegated to the 'run' function.