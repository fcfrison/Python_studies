# Quando é feita a importação de um módulo, antes de se alocar um novo espaço
# na memória, é feita uma verificação no 'system cache' e, caso o módulo que
# se deseja importar não esteja presente em tal local, então é feita a alocação
# de memória. Após isso, é inserida uma referência no 'system cache' e no escopo 
# global do módulo. Qual a vantagem disso? Se a mesma importação for efetuada em 
# vários módulos, a referência de memória será a mesma. 
import fractions
import sys
# Verificando a relação de todos os módulos carregados no 'system cache'
print(sys.modules['fractions'])
# Verificando alguns atributos, classes e métodos (funções) ligados ao módulo 'fractions'. 
print(dir(fractions))
fractions.__name__

# Sendo o módulo um tipo de dado, ele deve "viver" em algum lugar. Ou seja, ele
# deve possuir características que lhe são próprias. Ele vive aqui:
from types import ModuleType
print(isinstance(fractions,ModuleType))
print(type(ModuleType))

# Sendo módulo um objeto que pertence a uma classe, é possível instanciá-lo. 
modulo_qualquer = ModuleType('modulo_qualquer','Criando um módulo qualquer')
# É possível se inserirem atributos e métodos. 
modulo_qualquer.pi = 3.14
modulo_qualquer.metodo_unico = lambda: print("Hello World")
print(modulo_qualquer.metodo_unico())
