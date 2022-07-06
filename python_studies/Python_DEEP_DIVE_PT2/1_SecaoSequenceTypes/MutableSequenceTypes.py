'''
8. Mutable Sequence Types - Coding
'''
lista = list(range(5))
# clear()--> limpa a sequência, porém mantém o endereço de memória para a qual ela aponta. 
print(id(lista))
lista.clear()
print(id(lista))


l = [1,2,3]
print(id(l))
# Ao fazer uma atribuição, cfme a q segue abaixo, está se fazendo c/q 'l' aponte para um 
# endereço de memória diferente.  
l = [1,2,3,4]
print(id(l))

# Já a se utilizar um método como 'append', está se mudando o objeto, mas o endereço de memória do objeto 
# continua sendo o mesmo. 
def funcao(l:list):
    l.append('None')
print(l)
funcao(l)
print(l)

# Outro método aplicável a sequências, que muda as mesmas é 'extend'.
print(id(l))
print(l)
l.extend((5,6,7,8))
print(id(l))
print(l)

# O método 'pop' também muda a sequência sem alterar o endereço de memória. 
print(l)
l.pop()
print(l)
# O método 'insert' funciona da mesma forma (sem alterar o endereço).
print(id(l))
l.insert(2,'felipe')
print(l)
print(id(l))

# O método reverse também funciona da mesma forma. 
print(id(l))
l.reverse()
print(l)
print(id(l))

# O método copy copia o endereço da sequência e aloca um novo espaço de memória.
l2 = l.copy()
print(id(l2))
