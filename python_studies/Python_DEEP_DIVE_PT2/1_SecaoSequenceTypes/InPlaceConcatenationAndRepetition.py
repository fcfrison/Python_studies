'''
Aula 18. In-Place Concatenation and Repetition
'''
lista_1 = [1,2,3,4]
lista_2 = [5,6,7,8]
print(f'id(lista_1) = {id(lista_1)}, id(lista_2) = {id(lista_2)}')

# Concantenação de listas (estruturas mutáveis) gera um novo id na memória.
lista_1 = lista_1 + lista_2
print(f'id(lista_1) = {id(lista_1)}')

# Já concantenação in place de listas (estruturas mutáveis) ñ gera um novo id na memória.
lista_3 = ['a','b','c']
lista_1 += lista_3
print(f'id(lista_1) = {id(lista_1)}')
print(lista_1)

