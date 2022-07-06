'''
Aula 45. Sorting Iterables
'''
# Vou utilizar dataclasses.dataclass ao invés de __init__. É importante se destacar
# que isso não está na aula. 
from  dataclasses import dataclass
import random


@dataclass
class RandomInts:
    '''
    Classe que gera um conjunto aleatório de valores. 
    '''
    length: int
    seed: int = 0
    lower: int = 0
    upper: int = 10

    def __len__(self):
        return self.length
    def __iter__(self):
        return self.RandomIterator(self.length, self.seed, self.lower, self.upper)

    class RandomIterator:
        '''
        Classe que gera o iterador. 
        '''
        def __init__(self,length: int,seed: int,lower: int, upper: int):
            self.length = length
            self.seed = seed
            self.lower = lower
            self.upper = upper
            self.num_requests = 0
            random.seed(seed)
        def __iter__(self):
            '''
            Método especial que indica ao interpretador que RandomIterator é um
            objeto que pode ser iterado.
            '''
            return self
        def __next__(self):
            '''
            Método especial que informa ao interpretador que RandomIterator é 
            um iterador. 
            '''
            if self.num_requests>=self.length:
                raise StopIteration
            else:
                result = random.randint(self.lower, self.upper)
                self.num_requests+=1
                return result
aleatohrio = RandomInts(10)
for number in aleatohrio:
    print(number)

# Para colocar em ordem, basta utilizar a função intrínseca 'sorted'. 
sorted(list(aleatohrio))