'''
Sometimes shared resources can become problematic. The bellow code presents 
problems that can occur.

Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''
import ctypes
import multiprocessing
 
def deposit(d_value:ctypes.c_int)->None:
    for _ in range(100_000):
        d_value.value += 1

def withdraw(w_value:ctypes.c_int)->None:
    for _ in range(100_000):
        w_value.value -= 1


def execute_transactions(t_value:ctypes)->None:
    process_1 = multiprocessing.Process(target=deposit,kwargs={'d_value':t_value}) # Instantiating process_1
    process_2 = multiprocessing.Process(target=withdraw,kwargs={'w_value':t_value})
    print(f'process_name = {process_1.name}')
    print(f'process_name = {process_2.name}')

    process_1.start()
    process_2.start()

    process_1.join()
    process_2.join()

if __name__=='__main__':
    trans_value = multiprocessing.Value(ctypes.c_int,500) # creating shared resource
    print(f'trans_value = {trans_value.value}')
    [execute_transactions(t_value=trans_value) for _ in range(10)] # executing multiple transactions
    print(f'trans_value = {trans_value.value}')
