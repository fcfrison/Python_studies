'''
Creating a simple assync function.

Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

import asyncio

async def say_hello():
    '''
    Simple coroutine that just returns "Hello world".
    '''
    return "Hello world!!"

fn_1 = say_hello()

el = asyncio.get_event_loop() # creating a instance of an event loop.
var_1 = el.run_until_complete(fn_1)
el.close()
