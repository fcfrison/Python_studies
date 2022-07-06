# '*args' dentro das funções: eles 'capturam' o resto e "jogam" dentro de 
# uma tupla.
def imprime(a, b, *args):
    print(a)
    print(b)
    print(args)
# *args pegará tudo que vier depois de 'a' e 'b'.
tupla = (item for item in range(1,11))
a,b,*c=tupla
imprime(a,b,c)
imprime(a,b,*c)

# Uma forma de se "forçar" que no mínimo um argumento seja passado é a seguinte:
def media(a,*args):
    tamanho = len(args) + 1
    total = sum(args) + a
    return total/tamanho

print(media(3,2,5,4,7))

# Outra forma de se "desempacotar" os itens de um iterável é o que segue abaixo:
def novo_imprime(a,b,c):
    print(a)
    print(b)
    print(c)

lista = list(range(0,3))
novo_imprime(*lista)