# O garbage colector é utilizado para limpar a memória em situações bem
# específicas. Em geral, não há necessidade para o garbage collector atuar, dado 
# # que quando o 'reference counting' de um endereço de memória é zerado, o 
# Python automaticamente libera tal endereço. Porém, quando há referência 
# circular, somente através do garbage colector é possível se limpar a memória. 

import ctypes
import gc # Esse é o módulo do garbage colector.

def ref_count(address: int):
    '''
    Função que retorna a quantidade de referências apontando para um endereço 
    de memória específico. 
    '''
    return ctypes.c_long.from_address(address).value

def object_by_id(object_id:int):
    '''
    Essa função itera pelos objetos que estão no garbage colector e 
    aponta se o objeto passado como argumento está ou não no GC.
    '''
    for obj in gc.get_objects(): # Método que lista os objetos no GC
        if id(obj)==object_id:
            return "Objeto encontrado"
    return "Objeto não encontrado"

# A situação em que um objeto constará no GC é quando houver referência
# circular, que é o que se mostrará abaixo.
class Homem:
    def __init__(self):
        self.b =Mulher(self) # Ao fazer, Mulher(self), está se utilizando a instância de Homem como o parâmetro 
                             # de Mulher(). Em outras palavras, está se criando uma instância de Mulher() em Homem, 
                             # mas ao mesmo tempo, está se armazenando a referência na memória à instância de Homem
                             # na classe Mulher. 
        print(
            f'Homem: self: {hex(id(self))}. self.b: {hex(id(self.b))}'
        )
class Mulher:
    def __init__(self, other):
        self.homem = other
        print(
            f'Mulher: self: {hex(id(self))}. self.homem: {hex(id(self.homem))}'
            )
# Desabilitando o garbage colector.
gc.disable()
my_var = Homem()

# Verificando alguns detalhes ligados às classes acima. 
print(hex(id(my_var.b))) # Endereço da instância Mulher(self).

print(hex(id(my_var.b.homem))) # Endereço da instância de Homem().

# Armazenando os endereços das instâncias criadas. 
id_homem = id(my_var)
id_mulher = id(my_var.b)

#Verificando quantas referências estão ligadas a cada endereço de memória. 
ref_count(id_homem)
ref_count(id_mulher)

object_by_id(id_homem)
object_by_id(id_mulher)

# Fazendo com o que my_var aponte para um local diferente de id_homem.
my_var=None

# A referência para o endereço id_homem!=0.
ref_count(id_homem)
ref_count(id_mulher)

# Logo, só através do GC para esvaziar esses espaços na memória. 
# Ativando o garbage collector manualmente. 
gc.collect()