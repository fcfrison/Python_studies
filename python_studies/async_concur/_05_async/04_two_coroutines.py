'''
The code below shows a more complex relation between two coroutines. 

Code related to the course "Programação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

import datetime
import asyncio

async def data_generator(quantity:int, queue:asyncio.Queue):
    '''
    Simple data generator.
    '''
    print("Start to put data in the queue...")
    for i in range(quantity):
        await queue.put((i, datetime.datetime.now()))
        await asyncio.sleep(0.01)
    print(f'{quantity} items are in the queue')


async def data_consumer(quantity:int, queue:asyncio.Queue):
    '''
    Simple data consumer.
    '''
    print("Start the processing of the data in queue...")
    processed = 0
    while not queue.empty():
        for _ in range(quantity):
            await queue.get()
            await asyncio.sleep(0.001)
            processed+=1
    print(f'{processed} items were processed')

async def main():
    total = 500
    queue = asyncio.Queue()
    await data_generator(quantity=total,queue=queue) # enchendo a fila 
    await data_generator(quantity=total,queue=queue)
    await data_consumer(quantity=queue.qsize(),queue=queue) # esvaziando a fila

if __name__=='__main__':
    el  = asyncio.get_event_loop()
    el.run_until_complete(main())
    el.close()
