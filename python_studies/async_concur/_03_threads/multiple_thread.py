import threading
import time

def main(object,n_times):
    objects = [object + "_" + str(item) for item in range(n_times)]
    
    thread_list = [
        threading.Thread(target=just_count,args=[item,n_times]) 
        for item in objects
    ] # creating a list of threads

    fn_1 = lambda x:x.start() # lambda function to start threads
    list(map(fn_1,thread_list)) # adding the threads to the thread pool.
    print("Outras coisas podem ser efetuadas no programa" + 
            " enquanto a thread vai sendo executada")
    
    fn_2 = lambda y:y.join() # lambda function to create a waiting point.
    list(map(fn_2,thread_list)) # the program execution stops here until all thread finish executing 
    
    print("Aqui, executa somente qdo a thread terminar a sua execução")

def just_count(object:str,n_times:int):
    '''
    Function that just iterates.
    '''
    for n in range(1,n_times):
        print(f'{n} {object}(s)')
        time.sleep(1)
if __name__=='__main__':
    main("thread",10)