'''
Coroutines are not the same as plain Python functions.
'''
import asyncio

async def coroutine_add(number:int):
    return number+ 1 # non-blocking Python code --> coroutine is not necessary

def add_one(number:int):
    '''
    Plain function.
    '''
    return number + 1

function_result = add_one(10)
print(type(function_result))

coroutine_result = coroutine_add(10)
print(type(coroutine_result))


coroutine_result = asyncio.run(coroutine_add(10)) # putting coroutine on an event loop.
print(type(coroutine_result))


