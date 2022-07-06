# Uma forma bastante comum de se utilizarem funções lambda é através da função
# intrínseca sorted().

print(sorted(['c','a','C','A']))

# Uma forma de se "corrigir" o sorteio acima é utilizando o parâmetro 'key'
# em conjunto com uma função lambda. 
sorted(['c','a','C','A'], key=lambda x:x.upper())

# É possível se colocar um dicionário em ordem.
sorted({'banana':58, 'uva':1,'abacaxi':500,})

# Porém, se houver o desejo de se colocar o dicionário em ordem a partir dos 
# valores, é preciso utilizar-se uma função lambda.
dict_1 = {'banana':58, 'uva':1,'abacaxi':500,} 
sorted(dict_1, key=lambda item: dict_1[item])

{'banana':58, 'uva':1,'abacaxi':500,}.values()

# Utilizando uma função sorted() para randomizar um resultado.
from random import random
random()
lista = [item for item in range(1,11)]
sorted(lista, key=lambda x:random())