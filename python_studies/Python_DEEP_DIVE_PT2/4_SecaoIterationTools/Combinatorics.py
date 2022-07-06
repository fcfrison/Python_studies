'''
Aula 89. Combinatorics - Coding (Product)
'''
# Calculando o produto cartesiano "na mão". 
import itertools
l1 = ['x1', 'x2', 'x3']
l2 = ['y1','y2']
for item in l1:
    for item_ in l2:
        print(f'({item},{item_})')

# É possível fazer o que está acima de maneira mais direta através de 
# itertools.products().
print(list(itertools.product(l1,l2)))

# A vantagem em se utilizar essa classe é que não há limitação no número de
# iteradores ou iteráveis passados como argumentos. 
l3 = list(range(1,4))
print(list(itertools.product(l1,l2,l3)))

# É possível definir um iterator que retorna o produto cartesiano dois conjuntos
# de valores da seguinte forma.

def matrix(n):
    '''
    Foi utilizado um 'yield from' pq os 'range' são iteradores. Ou seja, 
    caso se utilizassem apenas 'yield', teria que se utilizar loops for 
    para poder produzir os valor de range. 
    '''
    yield from itertools.product(range(1,n+1),range(1,n+1))
       
gen = matrix(4)
print(next(gen))
print(next(gen))
print(next(gen))


def matrix(n):
    '''
    Gerando um iterador sem yield from. 
    '''
    yield  itertools.product(range(1,n+1),range(1,n+1))
       
gen = matrix(4)
iterador = next(gen)
for item in iterador:
    print(item)

# Vamos imaginar que se deseje gerar um conjunto de pontos para 3 eixos. 
def grid(min_val, max_val, step, *, num_dimensions = 2):
    # Gerando um conjunto de pontos. 
    axis = itertools.takewhile(lambda x:x<=max_val, itertools.count(min_val,step))
    # Fazendo cópias do iterador. 
    axes = itertools.tee(axis, num_dimensions)
    # É preciso desempacotarem-se os iteradores gerados em 'axes'. 
    return itertools.product(*axes)

print(list(grid(0.5,1,0.25,num_dimensions = 3)))



