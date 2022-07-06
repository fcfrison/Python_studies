# Ao se passar um argumento para uma função, o que está se fazendo é passar
# o valor do endereço de memória em que está armazenado aquele argumento. 

def soma (a:int, b:int):
    print(f'a: {hex(id(a))},\nb: {hex(id(b))}')
    return a + b

var_1 = 5
var_2 = 10
print(f'var_1: {hex(id(var_1))},\nvar_2: {hex(id(var_2))}')
soma (var_1, var_2)