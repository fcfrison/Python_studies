# Em Python, os números inteiros não possuem tamanho fixo definido. Isso quer
# dizer que não há limites teóricos para o tamanho máximo de um inteiro. Em 
# outras palavras, o tamanho máximo de um inteiro está relacionado com a quantidade
# de memória física disponível. 
import sys
print(f'sys.getsizeof(0) = {sys.getsizeof(0)} bytes')
# O tamanho é de 24 bytes, dado que 0 é uma instância da classe 'int'. Ou seja, 
# esse é o espaço necessário para se armazenar tal instância da classe 'int'.
# No caso do inteiro 0, como ele não requer nenhum bit para ser representado, 
# esse espaço é exclusivamente utilizado para a representação do objeto. A 
# isso o professor da aula chamado de overhead.

print(f'sys.getsizeof(1) = {sys.getsizeof(1)} bytes')