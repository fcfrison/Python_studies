'''
Which one is faster: threads or processes?

Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

from concurrent.futures import thread
import datetime
import math

import multiprocessing
from concurrent.futures.process import ProcessPoolExecutor as Executor


def main():
    number_of_cores = multiprocessing.cpu_count() # número de cores no pc
    print(f'Ammount of cores : {number_of_cores}')
    start_time = datetime.datetime.now()
    with Executor(max_workers=number_of_cores) as executor:
        for n in range(1,number_of_cores+1):
            start = 50_000_000*(n-1)/number_of_cores
            end = 50_000_000*n/number_of_cores
            print(f'Core number {n} processing...starts at {start}, ends at {end}')
            executor.submit(fn=compute,start=start, end=end)
    elapsed_time = datetime.datetime.now() - start_time
    print(f'Elapsed time = {elapsed_time}')

def compute(end:int, start:int=1):
    pos = start
    while pos<end:
        math.sqrt((pos-1_000_000)**2)
        pos+=1
if __name__ == '__main__':
    main()
