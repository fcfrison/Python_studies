'''
Aula 156. Command Line Arguments
'''
# Para fazer o parse dos argumentos passados no terminal, é possível utilizar-se
# o pacote built-in argparse
import argparse
import sys
parser = argparse.ArgumentParser(description='Calcula a//b e a%b de dois inteiros.')
# Adicionando os argumentos que serão recebidos.
parser.add_argument('a', help="primeiro inteiro", type=int)
parser.add_argument('b', help="segundo inteiro", type=int)
# É possível, ao invés de se passarem os argumentos no terminal, se passarem no próprio
# programa.
args = parser.parse_args(['50','25'])
print(args.a)
print(args.b)
# Porém, e possível se passarem os argumentos a partir da linha de comando.
args = parser.parse_args()
print(args.a)
print(args.b)
