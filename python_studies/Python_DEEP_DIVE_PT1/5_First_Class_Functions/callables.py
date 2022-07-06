# Callables
callable(print)

# Todas os callables retornam valores, mesmo as funções que não tenham retorno.
result = print('Hello')
print(result)

# O método object.upper é callable, porém object.upper() não é um callable, dado 
# que esse método retorna um string, que não é um callable.
s = 'abc'
callable(s.upper)

# Classes também são callables.
from decimal import Decimal
callable(Decimal)
# A classe Decimal é callable, mas as instâncias criadas a partir dela, não.
decimal = Decimal('3.14')
callable(decimal)
# Porém, há instâncias que podem ser callables.

class MyClass:
    def __init__(self, x:int=0):
        print("Inicializando...")
        self.counter = x
    def __call__(self, x=1):
        '''
        Método especial que faz com que as instâncias da classe sejam callables.
        '''
        self.counter+=x
        print(f"Atualizando o contador em {x} unidades, sendo que counter ={self.counter}" )
a = MyClass(50)
callable(a)
a(25)