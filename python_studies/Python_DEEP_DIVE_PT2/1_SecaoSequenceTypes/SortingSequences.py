import random
'''
Aula 25. Sorting Sequences - Lecture
'''
# Para colocar em ordem uma sequência de elementos, é preciso se estabelecer
# um critério de comparação, a que se dá o nome de 'key'. A partir desse critério,
# é criado uma ordem natural. Para caracteres, por exemplo, essa ordem é definida
# pelo valor do code point na tabela Unicode.
print(f"'a'<'b' = {'a'<'b'}", f", ord('a') = {ord('a')}, ord('b') = {ord('b')}")

class Person:
    def __init__(self, idade):
        self.idade = idade
    @staticmethod
    def key(self):
        '''
        Função que define um critério de comparação entre as idades das pessoas.

        '''
        return self.idade
    def __repr__(self) -> str:
        return f'Person({self.idade})'
pessoa1 = Person(10)
pessoa2 = Person(30)
pessoas = [Person(random.randint(0,100)) for item in range(0,10)]
print(pessoas)
# A função sorted() utiliza a 'key' definida para ordenar a sequência.
sorted(pessoas,key = Person.key)
# A função sorted() gera um novo endereço de memória para o objeto retornado 
# por ela.
print(f'id(pessoas) = {id(pessoas)}, id(sorted(pessoas,key = Person.key)) = {id(sorted(pessoas,key = Person.key))}') 

# Existe também o método sort(), que é do tipo in-place, ou seja, ela altera o 
# iterável passado como argumento.
pessoas = [Person(random.randint(0,100)) for item in range(0,10)]
print(id(pessoas))
pessoas.sort(key = Person.key)
print(pessoas)
print(id(pessoas))

# Definindo um método para colocar objetos de determinada classe em ordem.
class MyClass:
    def __init__(self,nome,valor) -> None:
        self.nome = nome
        self.valor = valor

    def __repr__(self) -> str:
        return f'MyClass({self.nome}, {self.valor})'
    def __lt__(self, other):
        '''
        Método especial para comparar dois objetos da classe MyClass.
        '''
        return self.valor < other.valor
c1 = MyClass('c1',20)
c2 = MyClass('c2',20)
c3 = MyClass('c3',10)
c4 = MyClass('c4',10)
print(c1<c2)
# O método __lt__ é utilizado para fazer a comparação entre as instâncias.
sorted([c1,c2,c3,c4])

