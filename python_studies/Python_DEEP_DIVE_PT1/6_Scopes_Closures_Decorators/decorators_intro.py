# Aula 105 - Decorators.
from re import sub


def counter(fn):
    count = 0
    def inner(*args,**kwargs):
        # 'inner' é uma closure que possui duas variáveis livres associadas
        # a si: 'fn', 'count'. 
        nonlocal count
        count+=1
        print(f'A função {fn.__name__} foi chamada {count} vezes')
        # A função 'inner' retorna a execução da função passada como argumento.
        return fn(*args,**kwargs)
    return inner

def add(a:int, b:int)->int:
    # Ao iniciar o programa, 'add' aponta para o endereço de memória que contém
    # as instruções abaixo.
    return a+b
# Ao fazer add = counter(add), 'add' receberá o closure 'inner', que possui
# dois as variáveis livres, 'count', que aponta para 0 e 'fn', que aponta para 
# o 'add' definido acima. 
add = counter(add)

# Ao fazer 'resultado = add(2,3)', estará se atualizando o valor da variável 
# livre 'count' e estará a se acessar o endereço de memória da variável livre 'fn',
# que aponta para as instruções add(a:int, b:int) definidas acima. Logo, 'resultado'
# receberá 'a+b'.
resultado = add(2,3)
print(resultado)

# Se diz, então que a função 'add' foi 'decorated' com a função 'counter'. 
# Por isso, 'counter' pode ser chamada de um decorator. 

# Uma maneira de simplificar as coisas é utilizar '@'. 
@counter # Ou seja, ao invés de fazer subtracao = counter(subtracao), utiliza-se @counter. 
def subtracao(a:int, b:int)->int:
    '''
    Função que subtrai dois números.
    '''
    return a-b
subtracao(50,25)
# Repare-se que 'subtracao' aponta para 'inner'
print(subtracao.__name__)
print(help(subtracao))

# Para que a função que é envolvida pelo um 'decorator' possa ter a sua documentação
# mantida, deve-se fazer o seguinte na função 'decorator'. 


def counter_modificado(fn):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print(f'A função {fn.__name__} foi chamada {count} vezes')

        return fn(*args,**kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

def produto(a:int, b:int)->int:
    return a*b
# O que segue na linha abaixo equivale a @counter_modificado.
produto = counter_modificado(produto)
help(produto)

# Apesar dessa solução resolver o problema da documentação da função que é 
# envolvida por um 'decorator', há metadados que são perdidos (entre eles a
# a assinatura da função). Para resolver esses problemas, os programadores 
# que desenvolveram a linguagem Python criar o decorator 'wraps', que está em 
# functools.

from functools import wraps
def counter_wraps(fn):
    count = 0
    def inner(*args,**kwargs):
        nonlocal count
        count+=1
        print(f'A função {fn.__name__} foi chamada {count} vezes')

        return fn(*args,**kwargs)
    inner = wraps(fn)(inner)
    return inner


def potencia(a:int, b:int)->int:
    '''
    Funcao que calcula a**b.
    '''
    return a**b

potencia = counter_wraps(potencia)
help(potencia)


