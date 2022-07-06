'''
Importando manualmente o módulo 'module_1.py'.
'''
import os.path
import types
import sys

nome_modulo = 'module_1'
arquivo_modulo = 'module_1.py'
caminho_modulo = '.'
caminho_relativo = os.path.join(caminho_modulo,arquivo_modulo)
caminho_absoluto = os.path.abspath(caminho_relativo)
# Lendo o arquivo fonte.
with open(caminho_relativo,'r') as file:
    source_code = file.read()

# Criando um objeto da classe 'ModuleType'
modulo = types.ModuleType(nome_modulo)
# Especificando onde o módulo poderá ser encontrado.
modulo.__file__ = caminho_absoluto
# Criando uma referência em sys.modules, que é o dicionário em que se encontram 
# os nomes do módulos e a sua referência na memória.
sys.modules[nome_modulo] = modulo

# Compilando o código fonte. 
code = compile(source_code, filename=caminho_absoluto, mode='exec')

# Executando o código compilado e informando que os nomes existentes no escopo 
# global do módulo 'module_1.py' ficarão armazenados no 'namespace' de 'modulo'. 
exec(code,modulo.__dict__)

modulo.p_print()
