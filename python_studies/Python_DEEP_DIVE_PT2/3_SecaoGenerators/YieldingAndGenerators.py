'''
Aula 59. Yielding and Generator Functions
'''
# Uma classe simples implementada para representar um iterador.
import math
class FactIter:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.i >=self.n:
            raise StopIteration
        else:
            result = math.factorial(self.i)
            self.i+=1
            return result
fact_iter_1 = FactIter(5)
print(next(fact_iter_1))
print(next(fact_iter_1))
print(next(fact_iter_1))

# É possível se criar o processo de cálculo de um fatorial através de um generator.
# Um generator é uma função que possui a palavra reservada 'yield'.
def my_func():
    '''
    Essa função pode ser entendida como um gerador de 'generators'.
    '''
    print('linha 1')
    yield 'Pós linha 1'
    print('linha 2')
    yield 'Pós linha 2'

gen = my_func()
# Tanto o método __iter__ quanto o método __next__ foram definidos no generator.
print('__iter__' in dir(gen))
print('__next__' in dir(gen))
print(type(gen))
print(next(gen))
print(next(gen))

def my_name():
    yield 'Felipe'
    yield 'Conzatti'
    yield 'Frison'
gen = my_name()
print(next(gen))
print(next(gen))
print(next(gen))

# Outra forma de se produzir um programa que calcule fatoriais se dá através 
# de um generator.
def fact(n):
    for item in range(n):
        yield math.factorial(item)
gen = fact(5)
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

