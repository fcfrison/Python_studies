# Para parametrizar um decorator, é preciso que o decorator esteja envolvido
# em uma função que o retorne. 
def outer(reps):
    '''
    Função que envolve o decorator. Ela é chamada de decorator factory. 
    '''
    def timed(fn): # Decorator. 
        from time import perf_counter # Escopo não local.
        from functools import wraps # Escopo local.
        def inner(*args, **kwargs):
            total_elapsed = 0
            for item in range(reps):
                start = perf_counter() # Escopo não local.
                result = fn(*args, **kwargs) # Escopo não local.
                total_elapsed += perf_counter() - start # Escopo não local.
            avg_elapsed = total_elapsed/reps # Escopo local. 
            print(avg_elapsed)
            return result
        # Decorator em que os metadados da função original são mantidos. 
        inner = wraps(fn)(inner)
        return inner
    return timed

def soma(a:int, b:int)->int:
    return a+b
# Uma forma de se chamar o decorator parametrizado é:
timed = outer(20)
soma = timed(soma)
soma(30,25)

# Outra forma é:
soma = outer(20)(soma)
soma(30,25)

# Ou ainda, é possível se utilizar a seguinte notação. 
@outer(20)
def mult(a:int, b:int)->int:
    return a*b
mult(25,30)

# Utilizando funções mais simples, o esquema do factory decorator é o seguinte. 
def dec_factory(param):
    print("Executando dec_factory.")
    def decorator(fn):
        print(f"Executando decorator com 'param' = {param}")
        def inner():
            print("Executando inner")
            return fn()
        return inner
    return decorator 
def func_1():
    print("Executando func_1")
func_1 = dec_factory("Parêmetro 1")(func_1)
func_1()

# Outra sintaxe possível é:
@dec_factory('Parâmetro 2')
def func_2():
    print("Executando func_2.")
func_2()