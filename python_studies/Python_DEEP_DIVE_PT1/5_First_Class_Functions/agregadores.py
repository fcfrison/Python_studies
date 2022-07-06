'''
Aula 90.
Agregadores são funções que recebem uma sequência de valores (uma lista, tupla,
etc.) e retornam apenas um valor. Por exemplo: max, min, etc.
'''
# Exemplo:
max_value = lambda x,y: x if x>y else y
# Definindo uma função de alta ordem.
def _reduce(fn,sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result,x)
    return result
_reduce(max_value,list(range(0,25)))

# Ao invés de definir uma função agregadora, é mais direto utilizar 'reduce' do 
# módulo functools.
from functools import reduce
reduce(lambda x,y: x if x>y else y, range(0,51))
reduce(lambda x,y:x+y, range(0,51))
# Ao invés de se utilizar uma função lambda, é possível a utilização de uma 
# função built-in.
reduce(max,range(1,51))

# any -> retorna true se algum elemento for 'true'.
any([False,1,2,3,4])
# O equivalente a any() utilizando reduce().
reduce(lambda a,b:bool(a) or bool(b),[False,1,2,3,4])

#all -> retorna true se todos os elementos de um interável forem true.
all([0,1,2,3])
all([1,2,3])

# Encontrando o produto dos valores de um iterável. O argumento '1' equivale 
# ao "initializer". Ou seja, ao primeiro valor a ser considerado ao se iniciar
# a agregação.
reduce(lambda x,y:x*y, [1,2,3,4], 1)

# Encontrando o fatorial de n.
n=10
reduce(lambda x,y:x*y, range(1,n+1))



