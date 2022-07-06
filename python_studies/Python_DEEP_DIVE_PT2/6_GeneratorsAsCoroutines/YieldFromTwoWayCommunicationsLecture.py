'''
Aula Yield From - Two-Way Communications - Lecture
'''

# A forma padrão de se utilizar o yield from equivale a substituir 
def subgen():
    for i in range(10):
        yield i

def delegator():
    for value in subgen():
        yield value

gen = delegator()
print(next(gen))
print(next(gen))
print(next(gen))

# Ao invés de fazer o que está acima, podemos fazer:
def delegator():
    yield from subgen()
gen_1 = delegator()
next(gen_1)
next(gen_1)
next(gen_1)