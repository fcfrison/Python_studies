# Vamos imaginar que eu deseje importar o pacote 'math' sem 'import'. 
# Nesse caso, eu poderia utilizar 'importlib'.
import importlib
import sys

importlib.import_module('math')
# Isso faz com que 'math' esteja no dicionário sys.modules.
print('math' in sys.modules)
# Mas 'math' não está no namespace do presente módulo como um módulo. 
print('math' in globals())
# Portanto, é preciso inseri-lo no 'namespace' global. Uma forma de fazer isso é:
math2 = importlib.import_module('math')
# O que equivale a import math as math2
print(math2.sqrt(2))
# Para importar módulos, Python utiliza 'finders' e 'loaders'. 
# Um 'finder', caso encontre o módulo cujo nome é procurado, retornará um objeto
# da classe ModuleSpec.
print(math2.__spec__)
# Um loader, por sua vez, é algo que carregará o módulo, ou seja, fará todos os
# passos descritos no exemplo_3a.
print(importlib.util.find_spec('decimal'))


# Os 'finders' do Python olham, quando procuram por um módulo, para um conjunto 
# de locais. 
print(sys.path) 
# uma forma de se inserir um novo local para buscar módulos é sys.path.append(caminho).
