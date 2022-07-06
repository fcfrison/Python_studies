# Aula 107. Decorator Application (Timer)

def timed(fn): # Decorator. 
    from time import perf_counter # Escopo não local.
    from functools import wraps # Escopo local.
    def inner(*args, **kwargs):
        start = perf_counter() # Escopo não local.
        result = fn(*args, **kwargs) # Escopo não local.
        end = perf_counter() # Escopo não local.
        elapsed = end-start # Escopo local. 
        print(elapsed)
        return result
    # Decorator em que os metadados da função original são mantidos. 
    inner = wraps(fn)(inner)
    return inner


def fib_sequ_recursiva(n:int)->int:
    '''
    Função que calcula recursivamente o n-ésimo termo da sequência de Fibonacci.
    '''
    if n<=2:
        return 1
    else:
        return fib_sequ_recursiva(n-1)+fib_sequ_recursiva(n-2)

def fib_recursiva(n):
    '''
    Essa função faz com que exista apenas um retorno. 
    '''
    return fib_sequ_recursiva(n)

# Criando a função 'decorated'. 
fib_recursiva = timed(fib_recursiva)

# Calculando o 5 termo da seq. de Fibonacci e o tempo de cálculo. 
fib_recursiva(36)

# Implementando a função Fibonacci através de um loop.
def fib_loop(n):
    '''
    Calculando a sequência Fibonacci a partir de um loop.
    '''
    t1= 1 # Termo da posicao 1.
    t2= 1
    for i in range(3,n+1):
        tmp = t2
        t2=t1+t2
        t1 = tmp
    return t2

# Criando uma função "decorada".
fib_loop = timed(fib_loop)

fib_loop(36)

