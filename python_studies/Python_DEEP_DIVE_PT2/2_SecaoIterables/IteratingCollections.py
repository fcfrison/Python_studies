'''
Aula 34. Iterating Collections - Coding
'''
class Squares:
    '''
    Classe que representa um iterador que eleva o valor inicial ao quadrado.
    '''
    def __init__(self, lenght):
        self.i = 0 # Estabelece o valor inicial
        self.lenght = lenght
    
    def __len__(self):
        return self.lenght
    
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
    def __repr__(self):
        return f'{self.i}'
sq = Squares(5)
# Iterando sobre a classe definida acima.
while True:
    try:
        print(next(sq))
    except StopIteration:
        break