'''
Aula 106. The contextmanager Decorator - Coding
'''
# Um generator poderá ser utilizado para criar um context manager, se seguir o 
# seguinte tipo de estrutura.
'''
def gen(args):
    try:
        yield obj # Dentro do try, vão as instruções que normalmente iriam dentro do __enter__. 
    finally:
        # Dentro do finally, vão as instruções que normalmente iriam dentro do 
        __exit__.
'''
def open_file(fname, mode='r'):
    '''
    Função que "fabrica" um generator, implementado de forma a representar 
    um context manager. 
    '''
    print("abrindo arquivo...")
    # open() é um do tipo lazy.
    f = open(fname, mode)
    try:
        # A execução do código chegará dentro do try a partir do método especial
        # __enter__, pertencente à classe que cria o context manager.  
        yield f
    finally:
        # A execução do código chegará dentro do finally a partir do método especial
        # __exit__, pertencente à classe que cria o context manager.
        print("fechando o arquivo...")
        f.close()
class GenContextManager:
    def __init__(self, gen):
        self.gen = gen
    def __enter__(self):
        print("Retornando a instância de open().")
        return next(self.gen)
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("chamando next para fechar o arquivo... ")
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False
# Utilizando o generator a partir do context manager. 
gen = open_file('test.txt', 'w')
with GenContextManager(gen) as file:
    file.writelines('Felipe Frison')

# Para facilitar a escrita do que está acima, ou seja, p/ñ precisar criar a instância
# de open_file fora do with..., é possível a utilização de um decorator. 
def context_manager_decorator(gen_fn):
    def inner(*args,**kwargs):
        # Criando uma instância do generator.
        gen = gen_fn(*args,**kwargs)
        # Criando uma instância do context manager que "lida" com generators.
        ctx = GenContextManager(gen)
        return ctx
    return inner
# Criando de fato o decorator.
open_file = context_manager_decorator(open_file)

# Abrindo um arquivo a partir do decorator criado. 
with open_file('test.txt', 'w') as file:
    file.writelines('Felipe Frison')

# Ao invés de se escrever manualmente o decorator, é possível se utilizar um 
# decorator implementado na biblioteca padrão.
from contextlib import contextmanager

@contextmanager
def open_file(fname, mode='r'):
    '''
    Função que "fabrica" um generator, implementado de forma a representar 
    um context manager. 
    '''
    print("abrindo arquivo...")
    # open() é um do tipo lazy.
    f = open(fname, mode)
    try:
        # A execução do código chegará dentro do try a partir do método especial
        # __enter__, pertencente à classe que cria o context manager.  
        yield f
    finally:
        # A execução do código chegará dentro do finally a partir do método especial
        # __exit__, pertencente à classe que cria o context manager.
        print("fechando o arquivo...")
        f.close()
with open_file('test.txt') as f:
    print(f.readlines())

# É possível se utilizar o decorator 'contextmanager' para se escrever arquivos
# a partir do print().
import sys
@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file
    try:
        # Não será necessário se retornar nada. 
        yield
    finally:
        # Fechando o arquivo aberto e fazendo c/q a saída padrão seja o console.
        file.close()
        sys.stdout = current_stdout
with out_to_file('teste_out_to_file.txt'):
    print("Saída padrão alterada para teste_out_to_file.txt.")
