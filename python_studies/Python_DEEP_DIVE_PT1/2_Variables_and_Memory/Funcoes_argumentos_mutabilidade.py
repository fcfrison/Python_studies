# Os argumentos passados em uma função não representam valores, mas endereços
# de memória. Por isso, é preciso tomar cuidado na hora de se passar objetos
# mutáveis.

def process(s:str):
    print(f"Endereço de memória de s = {hex(id(s))}")
    s = s +'world'
    print(f"Endereço de memória de s = {hex(id(s))}")

string_1="Hello"
# Como 'string_1' é string, então ao fazer s = s +'world' está se alocando um novo espaço
# na memória. Porém, como o escopo é diferente, 'string_1' não é alterada.
process(string_1)
print(f"Endereço de memória de string_1 = {hex(id(string_1))}")
string_1

# Agora, se passará como argumento um objeto mutável, como uma lista. 
def modifica_lista(lista:list):
    print(f"Endereço de memória de lista = {hex(id(lista))}")
    lista.append(1000)
    print(f"Endereço de memória de lista = {hex(id(lista))}")

minha_lista = [1,2,3]
modifica_lista(minha_lista)
# Como listas são objetos mutáveis e ao se passar 'minha_lista' como argumento
# está se passando o endereço de memória, o que ocorre é que 'minha_lista' é
# alterada dentro da função.
print(minha_lista)
