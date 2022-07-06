'''
Aula 86. Grouping - Lecture
'''
# É possível iterar sobre um iterador (ou iterável) e organizar os itens 
# produzidos a partir de grupos. Para isso, é possível se utilizar itertools.groupby().
# Para realizar a organização dos grupos, duas regras básicas devem ser seguidas:
# a) deve se descrever uma função que apresente retorne a chave que identificada
# cada grupo. 
# b) os itens retornados pelo iterador ou iterável devem estar ordenados. 
# O objeto retornado por itertools.groupby() é uma tupla (lazy iterator) que possui 
# a chave e um sub_iterator. 

import itertools
# Utilizando itertools.groupby() sem definir a chave. 
tupla = (1,1,2,2,2,3,3,3,3,3)
iterador = itertools.groupby(tupla)
# O objeto retornado é uma tupla do tipo (chave, sub_iterator).
print(list(iterador))
it = itertools.groupby(tupla)
for group_key, sub_iter in it:
    print(group_key, list(sub_iter))

# Utilizando itertools.groupby() definindo uma chave. 
tupla_de_tuplas = (
    (1,'abc'),
    (1,'def'),
    (2,'pyt'),
    (2,'c#'),
    (3,'exp'),
    (4,'sql'),
    (4,'ghi')
)
it = itertools.groupby(iterable = tupla_de_tuplas,key=lambda x:x[0])
for group_key, sub_iter in it:
    print(group_key, list(sub_iter))

with open('cars_2014.csv', mode='r') as f:
    # Pulando as colunas do arquivo 'csv'.
    next(f)
    # Criando os grupos com base da montadora do carro.
    make_groups = itertools.groupby(f,lambda x:x.split(',')[0])
    # Iterando sobre o iterador 'make_groups', gerando os 5 primeiros yields.
    print(list(itertools.islice(make_groups,5)))

with open('cars_2014.csv', mode='r') as f:
    # Pulando as colunas do arquivo 'csv'.
    next(f)
    # Criando os grupos com base da montadora do carro.
    make_groups = itertools.groupby(f,lambda x:x.split(',')[0])
    # Contando a quantidade de modelos por montadora. 
    make_counts = ((key,len(list(sub_iter))) for key,sub_iter in make_groups)
    # Iterando sobre o iterador 'make_groups', gerando os 5 primeiros yields.
    print(list(make_counts))

