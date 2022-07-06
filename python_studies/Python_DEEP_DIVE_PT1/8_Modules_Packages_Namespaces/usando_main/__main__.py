# Aula 135.
# Ao chamar esse módulo de __main__.py e executar o diretório 'usando_main', 
# o Python executa esse módulo apenas. 
# Para executar o diretório inteiro, basta digitar no terminal python <nome do diretório>. 
# No caso deste módulo, basta executar 'python usando_main'.
print(f'carregando run.py: __name__ = {__name__}')
import modulo_1

if __name__ == '__main__':
    print('O modulo run.py foi executado diretamente. ')
else: 
    print('O modulo run.py foi executado indiretamente. ')