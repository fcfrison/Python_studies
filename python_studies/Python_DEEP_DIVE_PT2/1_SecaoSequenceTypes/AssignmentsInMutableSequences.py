'''
Aula 20. Assignments in Mutable Sequences
'''
# É possível se fazer 'assignments' através de slices.
lista = list(range(5))
print(lista, id(lista))
lista[0:2] = 'Felipe'
print(lista, id(lista))

# Para se deletarem itens em uma sequência, basta preencher o slice com uma 
# sequência vazia. 
lista[0:2] = ()
print(lista, id(lista))


# É possível se inserirem elementos através de slicing.
lista[3:3] = ('Ovo', 'batata', 'banana')
print(lista, id(lista))

