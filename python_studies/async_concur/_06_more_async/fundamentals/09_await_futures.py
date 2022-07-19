'''
The code below present a use case of a 'future' with
the 'await' reserved word.
'''

from asyncio import Future
import asyncio

def make_request() -> Future:
    '''
    Function that creates a Future task.
    '''
    future = Future() 
    asyncio.create_task(set_future_value(future))   # creating a task. By doing set_future_value(future), 
                                                    # we are not yet starting the execution of set_future_value, 
                                                    # cause it is a coroutine and not a regular function.
    return future

async def set_future_value(future) -> None:
    '''
    Coroutine that sets the value of the future object.
    '''
    print('right before sleep.')
    await asyncio.sleep(5)
    print('right after sleep.')
    future.set_result(42)

async def main():
    future = make_request()
    print(f'Is the future done? {future.done()}')
    value = await future # the execution of the task starts here.
    print(f'Is the future done? {future.done()}')
    print(value)
asyncio.run(main())