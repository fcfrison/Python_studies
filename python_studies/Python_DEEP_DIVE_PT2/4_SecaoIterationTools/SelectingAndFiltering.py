'''
Aula 76. Selecting and Filtering
'''
# Funções úteis ao se trabalhar com iteradores.
tupla = tuple(range(20))
pares = filter(lambda x:x%2==0, tupla)
pares = tuple(pares)
pares

# Se eu quiser os valores em que a afirmação for falsa.
import itertools
impares = itertools.filterfalse(lambda x:x%2==0, tupla)
impares = tuple(impares)
impares

# A classe takewhile() retorna os valores verdadeiros e para (stop) a iteração no primeiro
# valor falso.
menosDez = itertools.takewhile(lambda x:x<10, tupla)
menosDez = tuple(menosDez)
menosDez