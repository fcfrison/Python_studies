# Aula 135.
'''
Módulo que possui a função 'timeit'.
'''
from time import perf_counter
from collections import namedtuple
import argparse
Timing = namedtuple('Timing','repeats elapsed average')
print('Carregando timing...')

def timeit(code:str, repeats:int = 10)->namedtuple:
    '''
    Função que recebe uma porção de código, compila e executa o mesmo. 
    Isso é efetuado uma quantidade 'repeats' de vezes. A função cronometra 
    o tempo gasto para isso. 
    '''
    code = compile(code, filename='<string>',mode = 'exec')
    start = perf_counter()
    for _ in range(repeats):
        exec(code)
    end = perf_counter()
    elapsed = end - start
    average = elapsed/repeats
    return Timing(repeats,elapsed,average)

if __name__ == '__main__':
    print('Esse print só será executado se o módulo timing.py for executado diretamente no terminal.')
    # A intenção do que segue abaixo é chamar a função 'timeit' através do 
    # terminal e inserir parâmetros diretamente no terminal. 
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('code',type=str,help='Código que será compilado e executado.')
    parser.add_argument('-r','--repeats',type=str,help='Número de vezes para repetir o teste.')
    args = parser.parse_args()
    print(f'timing: {args.code}')
    print(timeit(code = str(args.code),repeats=int(args.repeats)))

