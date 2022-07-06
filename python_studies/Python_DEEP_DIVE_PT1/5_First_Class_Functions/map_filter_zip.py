# map function.
# map(func, *iterables)


l = [2,3,4]
def sq(x):
    return x**2

list(map(sq,l))

# Outro exemplo:
l1 = [1,2,3]
l2 = [10,20,30]

def add(x,y):
    return x+y

list(map(add,l1,l2))
list(map(lambda x,y:x+y,l1,l2))

# A função filter. 
# filter(func, iterable)
def is_par(x):
    if x%2==0:
        return True
    else:
        return False
list(filter(is_par,l1))

# Ou utilizando uma função lambda.
list(filter(lambda x:x%2==0,l1))

# 'filter' pode ser utilizado com None.
import numpy as np
list(filter(None,[0,1,'','felipe',None,True,False]))

# A função zip. 
# zip(*iterables)
# A função faz uma combinação um a um.
list(zip(l1,l2))
# Gerando uma lista arbitrária. 
l3=[x+y for x,y in zip(l1,l2)]
# Mantendo apenas os elementos ímpares.
list(filter(lambda x:x%2!=0,l3))
# Fazendo algo semelhante a partir de um list comprehension.
[item for item in l3 if item%2!=0]

