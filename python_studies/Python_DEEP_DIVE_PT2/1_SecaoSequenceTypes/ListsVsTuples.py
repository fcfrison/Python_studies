l1 =list(range(1,10))
t1 = tuple(range(1,10))
# Ao se fazer uma cópia de uma lista, considerando que ela é mutável, 
# Python aloca novo espaço na memória. 
l2 = l1.copy()
print(f'id(l1) = {id(l1)}, id(l2) = {id(l2)}')
# Ao se fazer uma cópia de uma tupla, considerando que ela é imutável, 
# não é alocada espaço novo na memória para o novo rótulo. 
t2 = tuple(t1)
print(f'id(t1) = {id(t1)}, id(t2) = {id(t2)}')

# Eficiência de armazenamento. 
# A alocação de tuplas em novos locais de memória é mais eficiente do que a de listas. 
#-------------------------------------------------------------------------
# ------------------ tuplas ------------------
#-------------------------------------------------------------------------
import sys
t = tuple()
prev = sys.getsizeof(t)
for i in range(100):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1}, items: {size_c}, delta = {delta}')
# Para a tupla de tamanho 'i+1', houve um incremento de 4 bytes em relação à tupla de 
# tamanho 'i', independemente do tamanho da tupla. 

#-------------------------------------------------------------------------
# ------------------ listas ------------------
#-------------------------------------------------------------------------
t = list()
prev = sys.getsizeof(t)
for i in range(100):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1}, items: {size_c}, delta = {delta}')
# Já para as listas, a variação é dependente do tamanho. 
# Agora, ao utilizar o método append, a alocação é bastante mais eficiente, uma vez que a cada 
# novo elemento, não necessariamente haverá nova alocação de memória. 
c = list()
prev = sys.getsizeof(c)
print(f'0 itens:{prev}')
for item in range(100):
    c.append(item)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1}, items: {size_c}, delta = {delta}')


