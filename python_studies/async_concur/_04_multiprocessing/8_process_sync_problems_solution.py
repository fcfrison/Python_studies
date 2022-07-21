'''
Sometimes shared resources can become problematic. The code bellow presents 
a solution to problems that existed in the file 8_process_sync....
Similarly to the threads case, a lock must be created.

Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''
import ctypes
import multiprocessing
 
def deposit(d_value:ctypes.c_int, lock:multiprocessing.RLock)->None:
    for _ in range(100_000):
        with lock: # this lock "locks" the resources as they are used by an specific process.
            d_value.value += 1

def withdraw(w_value:ctypes.c_int, lock:multiprocessing.RLock)->None:
    for _ in range(100_000):
        with lock:
            w_value.value -= 1


def execute_transactions(t_value:ctypes, lock:multiprocessing.RLock)->None:
    process_1 = multiprocessing.Process(target=deposit,kwargs={'d_value':t_value, 'lock':lock}) # Instantiating process_1
    process_2 = multiprocessing.Process(target=withdraw,kwargs={'w_value':t_value, 'lock':lock})
    print(f'process_name = {process_1.name}')
    print(f'process_name = {process_2.name}')

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

if __name__=='__main__':
    trans_value = multiprocessing.Value(ctypes.c_int,500) # creating shared resource
    r_lock = multiprocessing.RLock() # creating a lock object 
    print(f'trans_value = {trans_value.value}')
    [execute_transactions(t_value=trans_value, lock=r_lock) for _ in range(10)] # executing multiple transactions
    print(f'trans_value = {trans_value.value}')