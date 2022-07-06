# Tudo em Python é objeto. Funções também são objetos. 
from numpy import square


def quadrado(valor:int):
    return valor**2

# Sendo objetos, funções ocupam espaço na memória e possui referências, como
# qualquer outro objeto. Por exemplo, na função acima, 'quadrado' aponta para
# algum endereço na memória que conterá a instrução da função.  
a = quadrado
print(hex(id(a)))
b=quadrado
print(hex(id(b)))

# Ambas as referências, 'a' e 'b' apontam para o mesmo endereço de memória. 
a is b
a is quadrado
b is quadrado

# Sendo objetos, funções operam como quaisquer outros objetos: elas podem ser
# utilizadas como argumento, podem ser retornadas de outras funções, etc.

def cubo(a):
    return a**3

def select_function(fn_id:int):
    if fn_id == 1:
        return quadrado
    else:
        return cubo

# Fazendo com que 'f' aponte para o endereço de memória de 'quadrado'. 
f = select_function(1)   
f is quadrado

# Fazendo com que 'g' aponte para o endereço de memória de 'cubo'. 
g = select_function(2)
g is cubo

# É possível inclusive chamar a função a partir de 'g', dado que 'g' apenas aponta
# para o endereço de memória em que se encontram as instruções da função.
print(g(2))
