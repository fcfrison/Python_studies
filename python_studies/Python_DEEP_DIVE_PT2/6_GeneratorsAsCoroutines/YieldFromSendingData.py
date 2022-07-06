'''
Aula 128. Yield From - Sending Data - Coding
'''
import inspect
def echo():
    '''
    Generator que inverte os dados da sequência enviada a ele.
    '''
    while True:
        received = yield 'Retorno'
        print(received[::-1])

def delegator():
    e = echo()
    # O yield from já faz o prime de echo. Ou seja, já inicializa o mesmo com 
    # um next. 
    yield from e

d = delegator()
# Aqui o generator echo já é inicializado. 
print(next(d))
# Ambos os generators se encontram em estado suspenso. 
print(inspect.getgeneratorstate(d))
print(inspect.getgeneratorstate(inspect.getgeneratorlocals(d)['e']))
# É possível se enviarem dados ao generator echo através do generator 'delegator'.
print(d.send('Python'))

# Uma possível aplicação de corotinas com 'yield from' é fazer um parse de 
# 'nested items'. 
def flatten(curr_item):
    if isinstance(curr_item,list):
        for item in curr_item:
        # Esse 'yield from' inicializa um generator do tipo flatten(item) e retorna
        # ao 'caller' um item que não seja uma lista. 
            yield from flatten(item)
    else:
        yield curr_item
lista = [1,2,[3,[4,5,[6,7,8]],9,10],[11]]
for item in flatten(lista):
    print(item)

