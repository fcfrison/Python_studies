'''
Aula 75. Slicing - Coding
'''

# Utilizando o símbolo usual de slice, ou seja, lista[::], não é possível se 
# realizar slice em qualquer objeto iterável. Por exemplo, no objeto abaixo:
import math
def factorials(n:int)->math.factorial:
    for i in range(n):
        yield math.factorial(i)
#Porém, é possível se utilizar a função islice(), a ql retornará um iterador do tipo lazy:
import itertools
print(list(itertools.islice(factorials(5),3,5)))
