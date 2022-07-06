# No Python, as variáveis são passadas por referência. Ou seja, cada rótulo
# criado aponta para um endereço de memória. Cada endereço de memória pode ser
# referenciado inúmeras vezes. 
var_1=[100]
var_2=var_1

print(f'Endereço de memória de var_1 é {hex(id(var_1))}')

# Para verificar quantos rótulos estão apontados para o mesmo endereço de memória, 
# basta fazer o seguinte:
import ctypes

def ref_count(address: int):
    '''
    Função que retorna a quantidade de referências apontando para um endereço 
    de memória específico. 
    '''
    return ctypes.c_long.from_address(address).value
ref_count(id(var_1))