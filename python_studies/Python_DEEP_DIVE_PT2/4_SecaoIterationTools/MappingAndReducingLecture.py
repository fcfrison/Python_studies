'''
Aula 82. Mapping and Reducing - Lecture
'''
# Uma forma alternativa de se escrever a função map() é.
import itertools
import functools


fn = lambda x:x**2
map_ = (fn(x) for x in [1,2,3,4])
print(list(map_))
# Alternativamente.
print(list(map(lambda x:x**2,[0,1,2,3,4,5])))

# A função map() aceita apenas funções com 1 parâmetro. Se 
# a função tiver dois ou mais parâmetros de entrada, então deverá se 
# utilizar a função starmap(), que possui funcionamento semelhante 
# à função map().
lista_ = [[1,2],[3,4],[5,6],[7,8]]
starmap_ = itertools.starmap(lambda x,y:x*y,lista_)
print(list(starmap_))

# A função itertools.accumulate(iterable,fn) retorna um lazy iterator que, 
# conforme for sendo iterado, vai retornando os valores acumulados. 
soma = lambda x,y:x+y
print(list(itertools.accumulate([1,2,3,4,5],soma)))

# É possível também utilizar a função reduce() p/realizar acumulações. Só que, 
# ao invés de um iterável, é retornado uma medida de resumo. 
print(functools.reduce(lambda x,y:x**y, list(range(2,5))))

# É possível também se iniciar a sequência de cálculos por outros valores.
# No caso abaixo, se iniciará pelo valor 10. 
print(functools.reduce(lambda x,y:x**y, list(range(2,5)),10))

