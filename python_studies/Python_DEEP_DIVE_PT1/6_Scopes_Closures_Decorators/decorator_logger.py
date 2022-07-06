'''
Aula 108
'''

# Será criado um decorator que cria um log das funções utilizadas. Ou seja, 
# quando uma função (que será decorada pelo decorator) for utilizada, será 
# criado um log da mesma. Esse log, no mundo real, poderia ser um registro
# em um banco de dados. 
def logged(fn):
    '''
    Decorator 'logged'.
    '''
    from datetime import datetime,timezone
    from functools import wraps

    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        # Ao fazer fn(*args), está se desempacotando 'args'. Se não fosse feito assim, 
        # então teríamos um elemento posicional: uma tupla. Ao se desempacotar, teremos
        # 'n' elementos. 
        result = fn(*args, **kwargs)
        print('{0}:called {1}'.format(run_dt,fn.__name__))
        return result
    inner = wraps(fn)(inner)
    return inner

def func_1():
    pass
# 'decorando' a 'func_1', em que 'func_1' passará a apontar para um endereço de 
# memória que tem as instruções de 'inner'. 
func_1 = logged(func_1)
func_1()

@logged # Decorando a função 'soma'.
def soma(*args):
    return sum(args)
soma(1,2,3)


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

# Definindo uma função que calcula o fatorial. 
def fact(n:int)->int:
    '''
    Calculando o fatorial. 
    '''
    from operator import mul
    from functools import reduce
    return reduce(mul,range(1,n+1))

# Encapsulando a função 'fact' em dois decorators.
fact = logged(fact)
fact = timed(fact)
fact(10)

# Encapsulando a função multiplicacao com dois decorators. 
def multiplicacao(a:int, b:int)->int:
    return a*b
multiplicacao = timed(logged(multiplicacao))
multiplicacao(3,2)

# Encapsulando a função potencia com dois decorators. 
@timed
@logged
def potencia(a:int,b:int)->int:
    return a**b
potencia(2,3)

# Ordem em que os decorators são chamados. 
def dec_1(fn):
    def inner():
        print('dec_1')
        return fn()
    return inner


def dec_2(fn):
    def inner():
        print('dec_2')
        return fn()
    return inner

# O que segue abaixo equivale a my_func = dec_1(dec_2(my_func)).
@dec_1 
@dec_2
def my_func():
    print("Running my_func.")
my_func()