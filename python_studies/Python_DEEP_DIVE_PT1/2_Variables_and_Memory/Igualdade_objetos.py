# Há duas comparações possíveis em Python: é possível se comparar o estado de
# um objeto e é possível se comparar também o endereço de memória de dois objetos.

var_1 = 100
var_2 = 100

# O comparador 'is' é utilizado para verificar se dois objetos possuem a mesma
# referência de memória. 
var_1 is var_2

# Para comparar os estados, utiliza-se o operador '=='.
var_1==var_2

# Exemplo 2:
a = [1,2,3]
b = [1,2,3]
# Para objetos mutáveis, como listas, não haverá referências compartilhadas. 
# Ou seja, não haverá diversos rótulos apontados para o mesmo endereço de memória.
a is b

a==b

# Outro ponto interessante é que 'None' é um objeto que possuirá o mesmo endereço
# de memória (independentemente de qts referências apontem para ele).
a = None
b = None
c = None
a is None
a is b
a is c

