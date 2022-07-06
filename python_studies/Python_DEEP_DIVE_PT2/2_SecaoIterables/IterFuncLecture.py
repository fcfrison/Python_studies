# Para iterar sobre um objeto, Python, em primeiro lugar, chama pela função iter(), 
# que verifica, primeiro, se o método __iter__  foi implementado. Tendo sido implementado,
# o interpretador verifica se o objeto retornado é um iterador. Em segundo lugar, não havendo
# implementação de __iter__, ou não sendo o objeto retornado um iterador, é chamado o método
# especial __getitem__, sendo retornado um iterador. A forma genérica de um iterator que itera 
# sobre uma sequência qualquer é a seguinte. 


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


