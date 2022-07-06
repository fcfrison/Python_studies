from  dataclasses import dataclass

@dataclass
class Squares:
    '''
    Sequência de valores. 
    '''
    _n : int

    def __len__(self):
        return self._n
    def __getitem__(self,s):
        '''
        Método especial __getitem__. 
        '''
        if s>=self._n:
            raise IndexError
        else:
            return s**2
quadrado = Squares(5)
# Apesar do método __iter__ não ter sido implementado em Squares, ao se chamar 
# a função iter(), um iterador é retornado. 
iterador = iter(quadrado)
print(type(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador))

# iter() funciona, porque um iterador como o que segue abaixo é criado. 
class SeqIterator:
    '''
    Iterador genérico para sequências. 
    Ao chamar iter(seq), em que 'seq' é uma sequência qualquer, e não encontrar 
    __iter__, é chamado procurado o método __getitem__. Tendo sido implementado,
    é, então, criado um objeto da classe SeqIterator.
    '''
    def __init__(self, seq):
        self.seq = seq
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        try:
            item = self.seq[self.index]
            self.index+=1
            return item
        except IndexError:
            raise StopIteration()
# Ou seja:
quadrado_1 = Squares(3)
iterador_manual = SeqIterator(quadrado_1)
print(iterador_manual.__next__())
print(iterador_manual.__next__())
print(iterador_manual.__next__())

