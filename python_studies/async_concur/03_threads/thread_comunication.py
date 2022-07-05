# Sometimes, it's possible to have some sort of dependency between 
# two or more threads. In this module, we'e going to study what to 
# do in such situations. 
from queue import Queue
from threading import Thread
import time
import colorama

def data_generator(queue):
    '''
    Function that generates data.
    '''
    for i in range(11):
        print(colorama.Fore.GREEN + f'Generated data{i}',flush=True), 
        time.sleep(0.5)
        queue.put(i)

def data_consumer(queue):
    '''
    Function that consumes data. 
    '''
    while queue:
        value = queue.get()
        print(colorama.Fore.RED + f'Consumed data {value + 2}',flush=True)
        time.sleep(1)
        queue.task_done() # For each piece of data consumed, a task is done. 
if __name__=='__main__':
    print('System ready to run')
    queue = Queue()
    th1 = Thread(target=data_generator,args=(queue,))
    th2 = Thread(target=data_consumer,args=(queue,))

    th1.start() # adding the threads to the thread pool.
    th1.join()
    # Thread 2 is going to start only once thread 1 is over. 
    th2.start()
    th2.join()

