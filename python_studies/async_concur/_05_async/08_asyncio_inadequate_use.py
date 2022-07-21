'''
Asynchronous processing is adequate for situations in which 
IO operations are necessary. On the other hand, when CPU-bound
operations are in high demand, asynchronous operations are inadequate.
The code below shows a situation where asyncio is used improperly.

Code related to the course "Programação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

import asyncio
from datetime import datetime
import math


def main():
    print('Asynchronous processing of CPU-bound operations')
    el = asyncio.get_event_loop()
    start_time = datetime.now()
    el.run_until_complete(compute(start=1,end=50_000_000))
    elapsed_time = datetime.now() - start_time
    print(f'elapsed_time = {elapsed_time}')

async def compute(end:int, start:int=1):
    while end>=start:
        math.sqrt((end-1_000_000)**2)
        end-=1

if __name__=='__main__':
    main()