'''
Aula 73. Aggregators - Coding
'''
# Tudo o que existe em Python é objeto e todos os objetos possuem um valor 
# booleano associado a si. Uma classe customizada, se não tiver o método __bool__
# ou o método __len__ especificados, será, por default, 'True'.
class Person:
    pass
personOne = Person()
print(bool(personOne))

class Person:
    def __bool__(self):
        return False

personTwo = Person()
print(bool(personTwo))
# Caso o método __bool__ não tenha sido implementado, Python procura pelo método
# __len__. 
class Person:
    def __len__(self):
        return 0
personThree = Person()
print(bool(personThree))

# Caso ambos os métodos tenham sido implementados, Python procurará primeiro 
# pelo método __bool__.
class Person:
    def __init__(self, lenght):
        self.lenght = lenght
    def __bool__(self):
        return True
    def __len__(self):
        return 0
personFour = Person(5)
print(bool(personFour))

# É possível se utilizar os métodos any() e all() para se verificar se, respectivamente,
# no mínimo um ou todos elementos de um iterável satisfazem uma condição qualquer.
# Verificando se todos os elementos de uma lista são números.
import numbers
listaOne = [1,2,3,4,5,"Banana"]
print(all(map(lambda x: isinstance(x,numbers.Number),listaOne)))
# Verificando se no mínimo um dos elementos de uma lista são números.
print(any(map(lambda x: isinstance(x,numbers.Number),listaOne)))

