'''
Working with one process.
Code related to the course "rogramação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''

import multiprocessing

print(f'Starting process.... process name: {multiprocessing.current_process().name}')

def func(arg):
    '''
    Arbitrary function.
    '''
    print(f'arg value: {arg}')

def main():
    pc = multiprocessing.Process(target=func,kwargs={'arg':'someting'})
    print(f'Starting new process.... process name: {pc.name}')
    pc.start() # adding the process to the execution pool.
    pc.join()

if __name__=='__main__':
    main()


