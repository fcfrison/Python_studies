'''
Aula 104. Generators and Context Managers - Coding
'''
# É possível se criar uma classe que implementa um Context Manager e que 
# trabalhe com um generator. 
# Imagine-se um iterator que possui uma estrutura como a que segue abaixo:

def my_gen():
    try:
        print('Criando um context e produzindo um objeto.')
        yield list(range(1,5))
    finally:
        print('Saindo do contexto e realizando a limpeza.')
# Criando uma instância de um generator. 
gen = my_gen()
next(gen)
try:
    next(gen)
except Exception as f_:
    print(f'{Exception}')

# Criando uma classe que implemente o protocolo de context managers e trabalhe 
# com generators.
class GenCtxManager:
    def __init__(self, gen_func) -> None:
        # Criando uma instância do iterador. 
        self._gen = gen_func()
    def __enter__(self):
        # Retornando o objeto produzido pelo iterador. 
        return next(self._gen)
    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            # Como o generator possui em si a parte de limpeza, esse next é 
            # qm chama isso. 
            next(self._gen)
        except StopIteration:
            # Se uma exceção do tipo StopIteration for levantada, então nada. 
            pass
        return False
with GenCtxManager(my_gen) as obj:
    print(obj)
