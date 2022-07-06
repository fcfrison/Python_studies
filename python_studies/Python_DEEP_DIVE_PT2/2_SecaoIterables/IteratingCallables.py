'''
Aula 49. Iterating Callables - Coding
'''
# Incrementando o callable.
def counter():   
    i=0
    def inc():
        nonlocal i
        i+=1
        return i
    return inc

# Incrementando um iterator simples para um callable qualquer. 
class CallableIterator:
    def __init__(self,iterator:callable):
        self.iterator = iterator
    def __iter__(self):
        return self
    def __next__(self):
        return self.iterator()
callable_ = counter()
iterador = CallableIterator(callable_)
for _ in range(3):
    print(iterador.__next__())

# Criando um iterador mais elaborado.
class CallableIterator:
    def __init__(self,callable_:callable, sentinela:int):
        self.callable_ = callable_
        self.sentinela = sentinela
        self.is_consumed = False

    def __iter__(self):
        return self
    def __next__(self):
        if self.is_consumed==True:
            raise StopIteration
        else:
            result = self.callable_()
            if result == self.sentinela:
                self.is_consumed = True
                raise StopIteration
            else:
                return result
callable_1 = counter()
iterador_1 = CallableIterator(callable_1,2)
for item in iterador_1:
    print(item)


# O que ocorre é que Python possui a função iter(callable, sentinel) que faz exatamente
# o que foi descrito acima
callable_2 = counter()
iterador_2 = iter(callable_2,5)
for item in iterador_2:
    print(item)