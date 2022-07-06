'''
Aula 156.
'''
# É possível se passarem argumentos através do terminal ao se executar um arquivo
# Python.
import sys
# 'sys.argv' "puxa" os argumentos passados através do terminal como strings.
print(sys.argv)

numbers = [int(item) for item in sys.argv if item.isnumeric()]
print(numbers)

