# Aula 85


def my_func(
    x: "x integer",
    a: int = 10,
    *args: "argumentos posicionais adicionais",
    c: "parametro keyword opcional" = 250,
    **kwargs: "parametros keyword adicionais"
):
    return a * x


class Homem:
    def __init__(self):
        self.peso = 75
        self.altura = 1.75

    def calc_imc(self):
        imc = self.peso / self.altura**2
        return imc


# Verificando os atributos ligados à função 'my_func'.
dir(my_func)

# nome da função
my_func.__name__

# tupla contendo valores posicionais default.
my_func.__defaults__

print(my_func.__kwdefaults__)

# __code__ retorna um objeto que possui propriedades.
my_func.__code__.co_varnames

# O módulo inspect
import inspect

inspect.isfunction(my_func)
inspect.ismethod(my_func)

homem = Homem()
inspect.isfunction(homem.calc_imc)
inspect.ismethod(homem.calc_imc)

inspect.signature(my_func)
for param in inspect.signature(my_func).parameters.values():
    print("Name:", param.name)
    print("Default:", param.default)
    print("Annotation:", param.annotation)
    print("kind:", param.kind)
