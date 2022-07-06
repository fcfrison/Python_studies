import time

def time_it(fn, *args, rep = 1, **kwargs):
    '''
    Função que mede o tempo de execução de uma função. 
    '''
    # para que a função possa executar corretamente os seus parâmetros, eles 
    # deverão ser desempacotados. Essa é a razão pela qual foi colocado
    # *args,**kwargs.
    start = time.perf_counter()
    for item in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()
    return end-start

time_it(print,1, 2, 3, 4, sep = ' - ', end = '***\n', rep=10)


