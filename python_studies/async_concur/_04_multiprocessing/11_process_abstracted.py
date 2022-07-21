'''
Instead of working with the 'multiprocessing' or 'threading' modules, it's possible 
to work with the 'concurrent' package, whose main advantage is to do the same stuff as the
above mentioned libraries with just one package.

Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

# from concurrent.futures.thread import ThreadPoolExecutor as Executor
from concurrent.futures.process import ProcessPoolExecutor as Executor # importing the process pool.
import time

def processing(char):
    print('[',end='',flush=True)
    str_ = '['
    for _ in range(10):
        print(f'{char}',end='',flush=True)
        str_ += char
        time.sleep(1)
    str_+=']'
    print(']',end='',flush=True)
    return str_

def main():
    with Executor() as executor:
        future = executor.submit(processing,'#')
    print(f'future result = {future.result()}')

if __name__=='__main__':
    main()