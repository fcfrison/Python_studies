'''
Creating a more complex assync function.

Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

import asyncio

async def a_little_more_complex_coroutine():
    print("Hello ...")
    await asyncio.sleep(5) # await is used when asynchronous functions are called.
    print("world")

el= asyncio.get_event_loop() # Instantiating an event loop.
el.run_until_complete(a_little_more_complex_coroutine()) # It's all right to execute an asynchronous functions considering an event loop.
print("Stuff happening after the execution of the coroutine.")
print("This piece of code is executed only after the el is complete. ")
el.close()