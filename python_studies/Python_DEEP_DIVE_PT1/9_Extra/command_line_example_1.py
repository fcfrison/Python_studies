# A ideia é que o argumento passado no terminal seja do tipo: --last-name, 
# --first-name. Ou seja, será passado algo como:
# python command_line_example_1.py --last-name Frison --first-name Felipe.
import sys
key = sys.argv[1::2]  #--> exclui o elemento na posição 0, vai até o fim de dois em dois.
value = sys.argv[2::2]
args = {k:v for k,v in list(zip(key,value))}
print(args)
# Capturando os valores passados em variáveis.
first_name = args.get('--first-name', None)
last_name = args.get('--last-name', None)
print(f'first_name: {first_name}, last_name: {last_name}')