'''
Aula 123. Using Decorators to Prime Coroutines - Lecture
'''

# Como sabemos que uma 'coroutine' sempre deverá, além de ter a sua instância 
# inicializada, ser 'primed', ou seja, deverá se dar um next(instancia_criada), 
# então faz td sentido do mundo trabalhar-se com um decorator. 
import inspect
def coroutine(gen_func):
    '''
    Criando uma closure para um decorator. Essa closure é responsável por instanciar

    '''
    def inner():
        g = gen_func() 
        next(g)
        return g
    return inner

def echo():
    while True:
        received = yield
        print(received)

# Criando o decorator. 
echo = coroutine(echo)

# Criando uma instância da coroutine 'echo'. 
inst_1 = echo()
inst_1.send("Hello world!")
inst_1.close()
print(inspect.getgeneratorstate(inst_1))

# Outra forma de se definir o decorator acima é:
@coroutine
def echoes():
    while True:
        received = yield "Retorno"
        print(received)
inst_2 = echoes()
print(inst_2.send("Hello world!"))
print(inst_2.send("Hello beautiful world!"))
inst_2.close()
print(inspect.getgeneratorstate(inst_1))