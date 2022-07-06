# Até agora, funções foram utilizadas como 'decorators'.
def dec_factory(parametro_1):
    print('Executando dec_factory.')
    def decorator(fn):
        print('Executando decorator.')
        def inner(*args, **kwargs):
            print(f'Executando inner: parametro_1 = {parametro_1}')
            return fn(*args, **kwargs)
        return inner
    return decorator

def func_1():
    print('Executando func_1')

decorator = dec_factory('parametro_1')
func_1 = decorator(func_1)
func_1()

# É possível a utilização de classe como 'decorators'. Abaixo segue o exemplo
# de uma classe qualquer (que não está funcionando como decorator ainda).
class MyClass:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def __call__(self, c):
        '''
        Método especial que faz com que toda a vez que uma instância da classe
        MyClass seja chamada, esse método seja chamado.
        '''
        print('chamando a= {0}, b={1} e c={2}'.format(self.a,self.b,c))

objeto_qualquer = MyClass(10,20)
objeto_qualquer(35000)

# Para se utilizar uma classe como decorator, o método especial __call__ irá 
# funcionar como um decorator. Assim:
class MyClass:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b
    
    def __call__(self, fn):
        '''
        Método especial que faz com que toda a vez que uma instância da classe
        MyClass seja chamada, esse método seja chamado. Aqui, ele está funcionando
        como um decorator. 
        '''
        def inner(*args,**kwargs):
            print('Executando inner.')
            print('Paramêtros passados no decorator factory: a = {0} e b = {1}'.format(
                self.a, self.b))
            result = fn(*args,**kwargs)
            return result
        return inner

def multiplicacao(a,b):
    return a*b

decorator_factory = MyClass(5,50)
multiplicacao = decorator_factory(multiplicacao)
multiplicacao(3,4)

# Outra forma de se utilizar o decorator é:
@MyClass(10,20)
def potencia(a,b):
    return a**b
potencia(2,3)

        