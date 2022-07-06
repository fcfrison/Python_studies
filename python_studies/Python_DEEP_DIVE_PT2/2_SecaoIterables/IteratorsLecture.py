'''
36. Iterators - Coding
'''
# Para que Python possa iterar sobre as instâncias de uma classe, que é classificada
# como um 'iterator', é necessário a utilização de dois métodos especiais:
# __next__ e __iter__. Em outras palavras, um 'iterator' é um objeto que possui essas
# duas classes. 
class Squares:
    '''
    Classe que representa um iterador que eleva o valor inicial ao quadrado.
    '''
    def __init__(self, lenght):
        self.i = 0 # Estabelece o valor inicial
        self.lenght = lenght
    def __next__(self):
        '''
        Método especial que promove a iteração. Esse método é chamado quando 
        a função next() é utilizada.
        '''
        if self.i>=self.lenght:
            raise StopIteration
        else:
            result = self.i**2
            self.i+=1
            return result
    def __iter__(self):
        '''
        O método __iter__ é um método protocolar que informa ao interpretador do 
        Python que os ojbetos da classe são iteráveis. 
        '''
        return self
    def __repr__(self):
        return f'{self.i}'

sq = Squares(5)
lista = [item for item in sq]
print(lista)

sq = Squares(3)
# Ao iterar sobre um objeto iterável, o "motorzinho" de Python faz por debaixo
# dos panos é o seguinte.
sq_iterator = iter(sq)
# Se o método __iter__ tiver sido criado, então isso significa que o desenvolvedor 
# está informando ao interpretador que aquele objeto é um iterável. Por isso, 
# a referência de memória utilizada é aquela retornada pelo método especial __iter__. 
while True:
    try:
        item = next(sq_iterator)
        print(item)
    except StopIteration:
        break

