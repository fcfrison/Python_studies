'''
Aula 114. Coroutines - Coding
'''

# Coroutines têm a ver a execução coordenada de rotinas, de forma que, a depender
# do programador, o código "salta" de rotina em rotina, sendo que as rotinas
# ficam suspensas eqto as demais são executadas. 
import collections


def produz_elementos(dq:collections.deque, n:int)->None:
    '''
    Função que insere elementos em uma estrutura de dados do tipo fila.
    '''
    for i in range(n):
        dq.appendleft(i)
        if len(dq)==dq.maxlen:
            print("fila cheia...")
            # Suspende a produção de elementos.
            yield
def consome_elementos(dq:collections.deque):
    '''
    Função que retira elementos em uma estrutura de dados do tipo fila.
    '''
    while True:
        while len(dq)>0:
            print('processando', dq.pop())
        print('fila vazia')
        yield
def coordenador():
    dq = collections.deque(maxlen=10)
    produtor = produz_elementos(dq, 25)
    consumidor = consome_elementos(dq)
    while True:
        try:
            next(produtor)
        except StopIteration:
            break
        finally:
            next(consumidor)
coordenador()
