from aplicacao_decorator import timed

def fib(n:int)->int:
    '''
    A sequência de Fibonacci utilizando recursão, sem qualquer tipo de 
    melhorias. 
    '''
    print('Calculando fib({0})'.format(n))
    return 1 if n<3 else fib(n-1) + fib(n-2)

fib(5)

# É possível a utilização de uma classe para melhorar o cálculo da sequência de 
# Fibonacci. 
print('Calculando a sequência de Fibonacci através da classe Fib.')
class Fib:
    def __init__(self):
        # self.cache é um dicionário do tipo 'posição na sequência':'valor'
        self.cache = {1:1,2:1}
    def fib(self,n):
        if n not in self.cache:
            print('Calculando fib{0}'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]
fib_sequence = Fib()
print(fib_sequence.fib(4))
print(
'''
\n
---------------------------------------------------------
Calculando a sequência de Fibonacci através de uma closure.
---------------------------------------------------------
\n
'''
)
# É possível se realizar o cálculo do n-ésimo elemento da sequência de Fibonacci
# através de uma 'closure'. 
def fibonacci():
    cache = {1:1,2:1}
    def calc_fib(n):
        if n not in cache:
            print('Calculando calc_fib{0}'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

calc_fib = fibonacci()
calc_fib(5)

print(
'''
\n
---------------------------------------------------------
Calculando a sequência de Fibonacci através de um decorator.
---------------------------------------------------------
\n
'''
)
# Criando um decorator para uma função que calculem sequências. 
def memoize(fn):
    cache = dict()
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memoize
def fib_recursao(n:int)->int:
    '''
    A sequência de Fibonacci utilizando recursão, sem qualquer tipo de 
    melhorias. 
    '''
    print('Calculando fib_recursao({0})'.format(n))
    return 1 if n<3 else fib_recursao(n-1) + fib_recursao(n-2)
fib_recursao(4)

@memoize
@timed
def fact(n):
    print("Calculando {0}!".format(n))
    return 1 if n<2 else n*fact(n-1)
fact(140)

# Há diversos fatores envolvidos na memoização, de forma que criar um decorator
# para isso pode se tornar algo muito complexo. Por isso, é muito mais fácil 
# trabalhar com um decorator presente no módulo 'functools', que faz exatamente
# o que o decorator 'memoize', acima, faz, com alguns cuidados adicionais. 
from functools import lru_cache
@lru_cache(maxsize=8)# Equivale a fib_sequencia =lru_cache(fib_sequencia)(maxsize=8)
def fib_sequencia(n):
    print("Calculando fib_sequencia{0}!".format(n))
    return 1 if n<3 else fib_sequencia(n-1) + fib_sequencia(n-2) 
fib_sequencia(8)
fib_sequencia(16)
fib_sequencia(5)