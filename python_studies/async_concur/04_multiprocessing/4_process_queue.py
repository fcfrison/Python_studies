'''
In addition to pipes, queues can also be used to communicate processes.
'''
import multiprocessing


def print_process_name():
    '''
    Print the process name.
    '''
    print(f'process name = {multiprocessing.current_process().name}')

def queue_loader(queue):
    '''
    This function is responsable for load the queue.
    '''
    queue.put('send something')

def queue_unloader(queue):
    '''
    This function is responsable for unload the queue.
    '''
    msg_received = queue.get()
    print(f'Received message = {msg_received}')

def main():
    queue = multiprocessing.Queue()
    process_1 = multiprocessing.Process(target=queue_loader, kwargs={'queue': queue})
    process_2 = multiprocessing.Process(target=queue_unloader, kwargs={'queue': queue})

    process_1.start() # Start the process’s activity.
    process_2.start()

    process_1.join()
    process_2.join()

if __name__=='__main__':
    main()