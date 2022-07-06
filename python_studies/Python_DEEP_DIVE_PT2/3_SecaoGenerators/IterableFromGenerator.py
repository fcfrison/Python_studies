'''
Aula 61. Making an Iterable from a Generator - Lecture
'''
# Generators são iteradores (iterators) e ñ iteráveis (iterable). 
# Isso pode ser um problema, uma vez que iteradores são "projetados"
# para iterarem e serem descartados. 
def squares(n:int):
    for i in range(n):
        yield i**2
sq = squares(5)
enum1 = enumerate(sq)
# Como enumerate() gera uma instância de um iterável do tipo lazy, isso 
# quer dizer que o iterador só será executado quando o método __next__ for 
# chamado. Isso quer dizer que pode haver um descompasso entre o retorno de
# enumerate e os valores do generator 'sq'. 
print(next(sq))
print(next(sq))
print(list(enum1))
# Para que isso não ocorra, a ideia é criar um iterável. Ou seja, algo que 
# "resete" a contagem do iterador toda a vez ele tenha sido chamado. 
class Squares:
    def __init__(self, n:int):
        self.n = n 
    def __iter__(self):
        '''
        Toda a vez que o método especial __iter__ for chamado, uma nova
        instância do iterador squares será retornada.
        '''
        return self.squares(self.n)
    def squares(self, n:int):
        for i in range(n):
            yield i**2
    

quadrado = Squares(5)
for item in quadrado:
    print(item)

for item in quadrado:
    print(item)