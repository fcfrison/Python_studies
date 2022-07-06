# Abaixo serão abordadas duas operações ligadas aos inteiros. 
# mod() e floor(). A função mod() se refere ao módulo de uma fração, que 
# ñ é a mesma coisa que o resto. Já a função floor() se refere à divisão floor. 
# Por exemplo: 7/2 = 3.5. floor(3.5) é igual ao primeiro inteiro menor de 3.5.
# Logo, floor(3.5) = 3. O símbolo de floor() é '//'. Já mod() é o valor que 
# completa a seguinte equação. 
# 7 = 2*(7//2)+ mod(3.5) => 7 = 2*3+mod(3.5)=>mod(3.5)=1. 
# Ou seja, a = b * (b//a) + b%a.
# Outro exemplo: -3.5. 
# 7//-2 = floor(-3.5)=-4. Para descobrir o mod(-3.5), temos que observar a seguinte
# equação.
# a = b * (b//a) + b%a
# 7 = -2 * (-7//2) + 7%-2 => 7%-2 = -1 = mod(-3.5).
import math

# floor division
math.floor(-3.5)
-7//2

# módulo
7%-2

# flor() != truncate
print(f'trunc(-2.0001) = {math.trunc(-2.0001)}')
print(f'floor(-2.0001) = {math.floor(-2.0001)}')

