'''
Aula 67. Yield From - Coding
'''
# É possível fazer a iteração de um "generator expression" através de 
# 'yield from'.
lista_1 = [0,1,2,3,4,5]
lista_2 = [6,7,8,9,10,11]

# Uma forma de se lerem os elementos das duas listas acima é:
def read_list():
    for lista in (lista_1,lista_2):
        for item in lista:
            yield item
list(read_list())

# Porém, ao invés de fazer dessa forma, é possível se fazer o seguinte:
def read_list_yield_from():
    for lista in (lista_1,lista_2):
        yield from lista
list(read_list_yield_from())
