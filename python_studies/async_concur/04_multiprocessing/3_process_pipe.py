'''
It's possible to communicate different processes throught a pipe.
'''
import multiprocessing


def print_process_name():
    '''
    Print the process name.
    '''
    print(f'process name = {multiprocessing.current_process().name}')

def pipe_sender(conn):
    '''
    This function is responsable for send something.
    '''
    conn.send('send something')

def pipe_receiver(conn):
    '''
    This function is responsable for receive something.
    '''
    msg_received = conn.recv()
    print(f'Received message = {msg_received}')

def main():
    conn_1, conn_2 = multiprocessing.Pipe(True) # Creating the pipe connections
    process_1 = multiprocessing.Process(target=pipe_sender, kwargs={'conn':conn_1})
    process_2 = multiprocessing.Process(target=pipe_receiver, kwargs={'conn':conn_2})

    process_1.start() # Start the process’s activity.
    process_2.start()

    process_1.join()
    process_2.join()

if __name__=='__main__':
    main()