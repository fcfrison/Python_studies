import threading
import time

def main(object,n_times):
    th = threading.Thread(target=just_count,args=[object,n_times]) # creating a thread
    th.start() # adding the thread to the thread pool.
    print("Outras coisas podem ser efetuadas no programa " + 
            "enquanto a thread vai sendo executada")
    
    th.join() # the program execution stops here until the thread finished executing 
    
    print("Aqui, executa somente qdo a thread terminar a sua execução")

def just_count(object:str,n_times:int):
    '''
    Simple function that iterates.
    '''
    for n in range(1,n_times):
        print(f'{n} {object}(s)')
        time.sleep(.5)
if __name__=='__main__':
    main("animal",3)
