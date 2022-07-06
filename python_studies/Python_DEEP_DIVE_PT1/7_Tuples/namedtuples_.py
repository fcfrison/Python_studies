# 120. Named Tuples.
# É possível se gerar tuplas que possuem como referência não a posição (ou o índice),
# mas nomes. Para isso, utiliza-se a função 'namedtuple', que retorna uma classe.
# Ela retorna uma classe, não uma instância de classe. Ou seja, a partir da classe
# retornada, será possível se criarem instâncias.

from collections import namedtuple

# Criando a classe Point_2D
Point_2D = namedtuple('Point_2D', ['x','y'])

# Criando uma instância de Point_2D.
pt1 = Point_2D(10,20)
for item in pt1:
    print(item)

pt2 = Point_2D(x=100,y=200)
for item in pt2:
    print(item)
# Acessando os elementos da tupla. 
print(pt2.x)
print(pt2.y)

# Para descobrir quais os nomes dos elementos da tupla. 
print(Point_2D._fields)

# Transformando a namedtuple em um dicionário.
print(pt2._asdict())