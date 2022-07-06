"""
Aula 28. List Comprehensions - Coding
"""
pares = [item for item in range(100) if item % 2 == 0]
print(pares)
# List Comprehensions podem ser pensadas como funções, afinal de contas, elas
# possuem escopo de memória próprio. No caso de nested list comprehensions,
# a list comprehension de dentro possui escopo diferente da que está fora.
# No caso da linha abaixo, 'i'pertence ao escopo não local da list comprehension
# externa e 'j' está no escopo local da list comprehension interna.
table_mult = [[i * j for j in range(1, 11)] for i in range(1, 11)]
print(table_mult)

# Nested loops.
l1 = ['a','b','c']
l2 = ['x','y','z']
nested_loop = [i + j for i in l1 for j in l2]
nested_loop
# O que está acima é equivalente a:
new_list = []
for i in l1:
    for j in l2:
        new_list.append(i + j)
# Nesse caso, há apenas um escopo local. 
print(new_list) 

# É possível se utilizar sentenças com 'if' dentro de nested loops.
l3 = ['1','2','3']
l4 = ['2','3','4']
nested_loop_1 = [i+j for i in l3 for j in l4 if i!=j]
print(nested_loop_1)

# Um cuidado a se tomar quando está a se trabalhar com list comprehensions é a
# questão dos escopos das variáveis. Vou começar por um exemplo que não envolve
# list comprehensions.
lista_lambdas = []
for i in range(1,6):
    lista_lambdas.append(lambda x:x**i)
# Como 'i' é uma variável não local, dado que a função lambda possui escopo local, 
# então todos os 'is' apontarão para o mesmo objeto. Na prática, isso significa 
# que todas as funções passadas serão iguais. 
print(lista_lambdas[0](2))
print(lista_lambdas[1](2))
# O mesmo raciocínio é aplicável para list comprehensions. 
funcs = [lambda x:x**i for i in range(1,6)]
print(funcs[0](2))
print(funcs[1](2))

# Para resolver esse problema, basta estabelecer um valor padrão para 'i'. 
# Ao fazer isso, a cada vez que o loop ocorre, 'i' apontará para um novo local 
# de memória, que será armazenado no escopo local através de 'p'.
funcs_ = [lambda x, p=i:x**p for i in range(1,6)]