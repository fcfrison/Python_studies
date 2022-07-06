def print_dict(header:str,d:dict)->None:
    print('\n\n----------------------------')
    print('*****{0}*****'.format(header))
    for key,value in d.items():
        print(f'key = {key}, value = {value}')
    print('----------------------------\n\n')

# Passando o dicionário que contém as variáveis globais deste módulo como 
# argumento de 'print_dict'.
print('--------Executando {0} --------'.format(__name__))
print_dict('modulo_1.globals',globals())
print("Fim da execução do {0}.py".format(__name__))