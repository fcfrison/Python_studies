'''
52. Reversed Iteration
'''
# Reversed iteration tem a ver com iteração reversa. Ou seja, começar a iteração
# de um objeto iterável de trás para frente.
import collections
_SUITS = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
_RANKS = tuple(range(2,11)) + tuple('JQKA')
Card = collections.namedtuple('Card', 'rank suit')

class CardDeck:
    '''
    Classe que representa um baralho de carta. Trata-se de um objeto iterável.
    '''
    def __init__(self):
        self.lenght = len(_SUITS)*len(_RANKS)
    
    def __len__(self):
        return self.lenght
    def __iter__(self):
        return self.CardDeckIterator(self.lenght)
    def __reversed__(self):
        '''
        Método especial para implementar a função intrínsenca reverse().
        '''
        return self.CardDeckIterator(self.lenght, reverse = True)
    class CardDeckIterator:
        '''
        Iterador.
        '''
        def __init__(self,lenght, reverse = False):
            self.lenght = lenght
            self.i = 0
            # É a partir desse atributo que se identifica o sentido da iteração.
            self.reverse = reverse
        def __iter__(self):
            return self
        def __next__(self):
            if self.i>self.lenght:
                raise StopIteration
            else:
                if self.reverse:
                    index = self.lenght - 1 - self.i
                # Seleciona o par necessário para formar uma carta. 
                else:
                    index = self.i
                suit = _SUITS[index//len(_RANKS)]
                rank = _RANKS[index% len(_RANKS)]
                self.i += 1
                return Card(rank,suit)

