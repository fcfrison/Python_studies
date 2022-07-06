'''
Aula 78. Infinite Iterators - Lecture
'''
# A classe count() é similar à classe range(). As diferenças são:
# - é um iterator infinito; 
# - trabalha c/números de quaisquer tipos.
import itertools
iteradorCount = itertools.count(2,0.25)
# Como itertools.count() é um iterador inifinito, é preciso utiliza-se algum 
# iterador que possa encerrar a sua iteração, assim que alguma condição for
# alcançada.
iteradorCount = itertools.takewhile(lambda x: x<=3,iteradorCount)
iteradorCount = tuple(iteradorCount)
print(iteradorCount)

iteradorCount_1 = itertools.count(2,0.25)
iteradorCountIsSlice = itertools.islice(iteradorCount_1,5)
tupleIteradorCount_1 = tuple(iteradorCountIsSlice)
print(tupleIteradorCount_1)

# A classe itertools.repeat() retorna o elemento passado como argumento
# infinitas vezes ou n vezes (neste caso, o nº de vezes deve ser passado como
# argumento).
nome = itertools.repeat("Felipe",10)
nome = tuple(nome)
print(nome) 
# O detalhe dessa classe é que todos os elementos apontam para o mesmo lugar 
# na memória.
fn = lambda x: id(x)
print(tuple(map(fn,nome)))

import decimal
decimal.Decimal("1/3")
iteradorCount = itertools.takewhile(lambda x: x<=3,iteradorCount)
