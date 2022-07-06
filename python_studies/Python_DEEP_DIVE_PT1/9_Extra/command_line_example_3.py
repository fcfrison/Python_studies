import argparse
parser = argparse.ArgumentParser(description='testando valores default e flags')
# Adicionando argumento. Nesse caso, apenas '--monty' deverá ser passado, sem 
# nenhum valor especificado. 
'''
parser.add_argument('--monty', action='store_const', const='Python')
# Adicionando um argumento com um valor default.
parser.add_argument('--name', default='John')
args = parser.parse_args()
print(args)
print(args.monty, args.name)
'''
# Criando uma flag com valor default. No caso abaixo, nenhum valor deve ser passado 
# junto com a '-v' ou '--verbose'. Além disso, foi definido como valor default 'False'.
# Ou seja, se não for passado '-v', então 'verbose=False'.
parser.add_argument('-v', '--verbose', action='store_const', const=True, default=False)
args = parser.parse_args()
print(args)