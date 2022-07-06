from functools import lru_cache
'''
Aula 15. Custom Sequences
'''

# Sequências são iteráveis, mas nem todos os iteráveis são sequências. 
# O tipo 'sequence' deve implementar no mínimo os seguintes métodos especiais:
# __len__ e __getitem__, que é um método que retorna um elemento, dado um índice. 
my_list = [0,'a',20,None,-5.31231]
print(my_list.__getitem__(1))
print(my_list.__len__())

# Implementando uma classe "boba", que poderia representar uma sequência.
# O fato de ter sido implementado os métodos especiais __len__ e __getitem__
# torna a classe Silly um objeto que representa uma sequência. 
class Silly:
    def __init__(self,n:int):
        self.n = n

    def __len__(self):
        '''
        O método especial __len__ necessariamente deve retornar um inteiro.
        '''
        print("__len__ foi chamado")
        return self.n

    def __getitem__(self, value):
        if value<0 or value>self.n:
            raise IndexError
        else:
            print(f'Você requisitou o valor {value}')
            return 'Essa é uma afirmação ligada à classe Silly'

silly = Silly(3)
print(len(silly))
# Ao incrementar um for loop na sequência 'silly', o método __getitem__ é automaticamente
# chamado, de forma que o parâmetro 'value' é automaticamente gerado pelo for loop.  
for item in silly:
    print(item)
# A forma como Python faz a iteração sobre uma sequência através de um ciclo 'for' 
# é utilizando o método especial __getitem__, conforme segue abaixo:
my_list = list(range(silly.n))
value = 0
while True:
    try:
        item = silly.__getitem__(value)
    except IndexError:
        break
    value += 1
    # Aqui abaixo, ficaria o restante das instruções do programa que está a utilizar
    # o 'for loop'.
    print(item)


# Implementando uma sequência com 'slice' e 'índice'. Ao se fazer algo do tipo
# silly[0:5], está a se chamar o método __getitem__ e se passando como argumento,
# no caso abaixo, para o parâmetro 'value', um objeto da classe 'slice'.
class Silly:
    def __init__(self,n:int):
        self.n = n

    def __len__(self):
        '''
        O método especial __len__ necessariamente deve retornar um inteiro.
        '''
        print("__len__ foi chamado")
        return self.n

    def __getitem__(self, value):
        if value<0 or value>self.n:
            raise IndexError
        else:
            print(f'Você requisitou o valor {value}')
            return 'Essa é uma afirmação ligada à classe Silly'





# Criando uma classe que represente a sequência de Fibonacci. 
class Fib:
    def __init__(self,n:int):
        self.n = n
    def __len__(self):
        '''
        Método especial que retorna o tamanho da sequência.
        '''
        return self.n
    def __getitem__(self,s):
        if isinstance(s, int):
            if s<0:
                s = self.__len__() + s
            if s<0 or s>self.__len__():
                # Essa parte do código garante que ao se utilizar um for loop, 
                # por exemplo, a sequência não será infinita. 
                raise IndexError
            else:
                return Fib.seq_fibonacci(s)
        else:
            # Se o objeto passado como argumento não for um inteiro, então será 
            # da classe 'Slice'. 
            range_tuple = s.indices(self.n)
            print(range_tuple)
            start,stop,step = range_tuple
            rng = range(start,stop,step)
            return [Fib.seq_fibonacci(item) for item in rng]
    @staticmethod
    @lru_cache(2*10)
    def seq_fibonacci(n:int)->int:
        '''
        Definição
        ---------

            Método que implementa a sequência de Fibonacci. Trata-se de um método
            de classe (e não de instância). 
        '''
        if n<2:
            return 1
        else:
            return Fib.seq_fibonacci(n-1) + Fib.seq_fibonacci(n-2)
        
seq_fib = Fib(3)
print(seq_fib[2])
print(list(seq_fib))
print(seq_fib[-2])
for item in seq_fib:
    print(item)
print(seq_fib[0:1])
# O que está acima equivale a:
print(seq_fib.__getitem__(slice(0,2,1)))