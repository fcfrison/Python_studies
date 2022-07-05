from concurrent.futures import thread
import datetime
import math

import threading
import multiprocessing


def main():
    number_of_cores = multiprocessing.cpu_count() # número de cores no pc
    print(f'Ammount of cores : {number_of_cores}')
    start_time = datetime.datetime.now()
    threads = []
    for n in range(1,number_of_cores+1):
        start = 50_000_000*(n-1)/number_of_cores
        end = 50_000_000*n/number_of_cores
        print(f'Core number {n} processing...starts at {start}, ends at {end}')
        threads.append(
            threading.Thread(
                target = compute,
                kwargs = {'start':start, 'end':end}
            )
        )
    [th.start() for th in  threads]
    [th.join() for th in  threads]
    elapsed_time = datetime.datetime.now() - start_time
    print(f'Elapsed time = {elapsed_time}')

def compute(end:int, start:int=1):
    pos = start
    while pos<end:
        math.sqrt((pos-1_000_000)**2)
        pos+=1
if __name__ == '__main__':
    main()
