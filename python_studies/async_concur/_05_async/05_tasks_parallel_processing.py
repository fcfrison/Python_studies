'''
It's possible to execute event loops in parallel, instead of a serial execution.

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
        print(f'Item {i} inserted in the queue')
        await asyncio.sleep(0.001)
    print(f'{quantity} items are in the queue')


async def data_consumer(quantity:int, queue:asyncio.Queue):
    '''
    Simple data consumer.
    '''
    print("Start the processing of the data in the queue...")
    processed = 0
    while not queue.empty():
        for _ in range(quantity):
            print(f'item consumed = {await queue.get()}')
            await asyncio.sleep(0.001)
            processed+=1
    print(f'{processed} items were processed')

def main():
    total = 1_000
    queue = asyncio.Queue()
    el = asyncio.get_event_loop()

    task_1 = el.create_task(data_generator(total,queue)) # creating a task related to an event loop
    task_2 = el.create_task(data_generator(total,queue))
    task_3 = el.create_task(data_consumer(total*2,queue))

    tasks = asyncio.gather(task_1,task_2,task_3)
    el.run_until_complete(tasks)

if __name__=='__main__':
    main()
