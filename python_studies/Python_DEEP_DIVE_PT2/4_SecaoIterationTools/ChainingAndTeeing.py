'''
Aula 81. Chaining and Teeing - Coding
'''
import itertools
# A classe itertools.chain() permite que se execute uma sequência de iterators. 
# Poderia se criar um iterator semelhante a ela da seguinte forma.
def chain_iterables(*iterators):
    for iterator in iterators:
        yield from iterator
l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))
for item in chain_iterables(l1,l2,l3):
    print(item)

# O que está acima, equivale a:
l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))
for item in itertools.chain(l1,l2,l3):
    print(item)
# Vamos imaginar que nós tenhamos o seguinte iterator.
def squares():
    print('yielding 1st item')
    yield (i**2 for i in range(4))
    print('yielding 2nd item')
    yield (i**2 for i in range(4,8))
    print('yielding 3rd item')
    yield (i**2 for i in range(8,12))
# Para poder utilizá-lo com itertools.chain(*args), será preciso desempacotá-lo. 
for item in itertools.chain(*squares()):
    print(item)
# O que pode ser problemático, já que o desempacotamento do iterator é 'eager'. 
# Ou seja, é executado __next__ em todos os yield de squares() para só depois
# começar a iteração dentro de cada generator. 
# Para resolver esse problema da execução 'eager', é possível a utilização do método de classe
# from_iterables().
for item in itertools.chain.from_iterable(squares()):
    print(item)

# Outro exemplo:
l1 = (i**2 for i in range(4))
l2 = (i**2 for i in range(4,8))
l3 = (i**2 for i in range(8,12))
list_ = [l1,l2,l3]
for item in itertools.chain.from_iterable(list_):
    print(item)


# É possível se fazer cópias do mesmo iterador através da função itertools.tee.
def squares(n):
    '''
    Generator squares.
    '''
    for i in range(n):
        yield i**2
gen = squares(5)
# Criando 3 cópias de 'gen'.
iters = itertools.tee(gen,3)
# Uma tupla de iteráveis é retornada. 
print(iters)
print(type(iters))
