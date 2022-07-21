'''
Sometimes it's useful to create an event loop "manually", instead
of relying on methods like asyncio.run, which does the heavily lifting of
creating and managing the event loop. 
'''

import asyncio

async def main():
    await asyncio.sleep(1)

loop = asyncio.new_event_loop() # Instantiating a event loop.

try:
    loop.run_until_complete(main()) # takes a courotine and run until completes.
finally:
    loop.close()# even if an exception was raised, it's important to release resources
                # that eventually were destined to the event loop.