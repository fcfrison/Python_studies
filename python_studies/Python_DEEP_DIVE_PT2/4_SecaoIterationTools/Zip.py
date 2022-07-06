'''
Aula 85. Zipping - Coding
'''

# A classe zip() retorna um lazy iterator que une os elementos produzidos 
# por um iterador ou iterável em uma tupla, a depender da ordem em que 
# eles são produzidos. Sempre será tomado como referência o iterador ou iterável
# de menor tamanho. 
import itertools


print(tuple(zip([1,2,3],range(10))))

# É possível, ao invés de fazer o zip considerando o menor iterador ou iterável, 
# utilizar o maior deles como referência. Para isso é possível utilizar ziplongest.
print(tuple(itertools.zip_longest([1,2,3],range(10))))

# É possível se escolher o valor a ser utilizado para preenchimento. 
print(tuple(itertools.zip_longest([1,2,3],range(10),fillvalue="FELIPE")))

