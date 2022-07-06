# Abaixo, 'a' é uma variável de escopo global e 'b' é uma variável de escopo local.
# Ao não encontrar 'a' no escopo local, o Python vai para o escopo global procurar
# por ela. Após isso, ele vai para o escopo built-in. Caso ela não seja encontrada, 
# então é gerado erro. 
a = 800
print(f'id do escopo global = {id(a)}')
def _print(b):
    print(id(a))
    print(b)
_print(52)

# Outro exemplo. 
def _print_1(b):
    a=800
    print(f'id do escopo local = {id(a)}')
    print(b)
# Agora, ao fazer a=100, é criado uma nova relação 'label' <->'espaço de memória'
# no escopo local. Prova disso é que esse id é diferente do id de 'a' no escopo
# global.
_print_1(666) 

# Segue uma série de exemplos.
def func2():
    a=250
    print(a)
# No caso acima, dado que está se dando um valor para 'a' dentro da função, 
# Python irá assumir que 'a' é local. 

# É possível se declararem variáveis de escopo global dentro da função. 
def func3():
    global a
    print(a)
    # Ao declarar 'a' como global, alterações que ocorrerem dentro da função 
    # irão alterar eventuais referências a ela fora da função.
    a=100
func3()
print(a)

# Python tem um comportamente diferente se comparado a Java. Em um loop 'for', por 
# exemplo, a variável criada para fazer o lugar não possui escopo local. 
for i in range(3):
    print(i)
print(i)
