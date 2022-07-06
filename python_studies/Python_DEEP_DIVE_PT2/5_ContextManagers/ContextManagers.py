'''
Aula 98. Context Managers - Coding
'''
# A lógica de funcionamento de context managers se assemelha à de try...except...finally.
from unicodedata import name


try:
    10/0
except:
    print("Uma exceção ocorreu")
finally:
    print("Essa linha de código sempre será executada.")

# Context manager é um tipo de protocolo efetivado em uma classe. Ele basicamente
# consiste de dois métodos especiais: __enter__ e __exit__. 
# O método especial __exit__ sempre será chamado, independentemente do que ocorra
# dentro do método __enter__. Por exemplo:
with open('test.txt','w') as file:
    print("Dentro de 'with': o arquivo foi fechado? ", file.closed)
print("Fora de 'with': o arquivo foi fechado? ", file.closed)

# A função open(), de alguma forma, possui os métodos especiais do protocolo
# de 'context managers' implementados. 

# Implementando uma classe que implementa o protocolo de 'context managers'. 
class MyContext:
    def __init__(self):
        self.obj = None
    def __enter__(self):
        '''
        Método especial que permite que se entre no context manager.
        '''
        print("Entrando no context ...")
        self.obj = 'the return object'
        return self.obj
    def __exit__(self, exec_type, exc_value, exc_tb):
        '''
        Método especial que implementa as ações que serão tomadas ao se sair 
        do manager context. 
        '''
        print("Saindo do context...")
        if exec_type:
            print(f'***Ocorreu ERRO: {exec_type}, {exc_value}***')
        # Ao retornar falso, está a se "dizendo" ao Python que o erro deverá ser 
        # levantado. 
        return False
# Nas linhas abaixo, se simulará o que ocorreria se estívessemos a utilizar o 
# 'with'. 
ctx = MyContext()
file = ctx.__enter__()
ctx.__exit__(exec_type=ValueError.__class__, exc_value=ValueError, exc_tb=None)

# Utilizando o 'with' de uma maneira mais explícita.
ctx = MyContext()
print('Contexto criado...')
with ctx as file:
    print("Dentro do 'with'...")
    print(file)
    #raise ValueError("uma mensagem qualquer")

class Resource:
    def __init__(self,name):
        self.name = name
        self.state = None

class ResourceManager:
    def __init__(self,name):
        self.name = name
        self.resource = None
    
    def __enter__(self):
        print('Entrando no contexto.')
        self.resource = Resource(self.name)
        self.resource.state = 'Criado'
        return self.resource
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('Saindo do contexto.')
        self.resource.state = "Destruído"
        if exc_type:
            print("Ocorreu erro.")
        return False
with ResourceManager('spam') as obj:
    print(f'{obj.name} = {obj.state}')
print(f'{obj.name} = {obj.state}')

# Exemplo de classe para criar um context manager para abrir e fechar arquivos. 
class File:
    def __init__(self, name, mode):
        print("Criando uma instância de File.")
        self.name = name
        self.mode = mode
    
    def __enter__(self):
        print("Abrindo arquivo...")
        self.file = open(self.name, self.mode)
        return self.file
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("Fechando arquivo...")
        self.file.close()
        return False
with File('test.txt','w') as f:
    f.write("Escrevendo uma linha em um arquivo de texto.")