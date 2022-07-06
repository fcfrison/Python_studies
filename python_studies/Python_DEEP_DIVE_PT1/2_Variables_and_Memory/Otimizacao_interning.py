# Internalização de inteiros:
# Números na faixa [-5,256] são internalizados automaticamente pelo Python quando
# algum script é executado. Ou seja, tais números são armazenados automaticamente
# na memória, de forma que eventuais identificadores que façam referência a eles
# simplesmente apontarão para um endereço de memória já existente.

num_1 = 5
num_2 = 5
print(hex(id(num_1)))
print(hex(id(num_2)))

print(num_1 is num_2)

# Valores que extrapolem a faixa [-5,256] terão alocação própria de memória.
num_3 = 257
num_4 = 257
print(hex(id(num_3)))
print(hex(id(num_4)))

print(num_3 is num_4)


# Internalização de strings.
# Por padrão, identificadores (nomes de funções, de variáveis, de classes, etc.) 
# são internalizados quando um script escrito em Python está rodando. 
# Outro detalhes é que qualquer string que pareça um identificador é internalizada. 
a = 'hello'
b = 'hello'
a is b

c= 'hello world'
d = 'hello world'
print(f'id(c) = {id(c)}, id(d) = {id(d)}')

# No entanto, ainda que uma string não respeite as regras para ser um identificador,  
# é possível arbitrariamente se internalizarem strings específicas.
import sys
e = sys.intern('Hello world!')
f = sys.intern('Hello world!')
g = 'Hello world!'
print(f'id(e) = {id(e)}, id(f) = {id(f)}, id(g) = {id(g)}')
print(e==f)
print(e is f)
