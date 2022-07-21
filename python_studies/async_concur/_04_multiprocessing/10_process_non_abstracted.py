'''
Creating a simple process algorithm without using 
process abstraction methods. 

Code related to the course "Programação Concorrente e Assíncrona com Python". 
Available at https://www.udemy.com/course/programacao-concorrente-e-assincrona-com-python/
'''
import multiprocessing
import time

def processing():
    print('[',end='',flush=True)
    for _ in range(10):
        print('#',end='',flush=True)
        time.sleep(1)
    print(']',end='',flush=True)

def main():
    th_1 = multiprocessing.Process(target=processing)
    th_1.start()
    th_1.join()

if __name__=='__main__':
    main()