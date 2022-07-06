# Tuplas não podem ser modificadas, por isso, a questão é: como fazer para 
# "aproveitar" valores existentes em uma tupla. 
from collections import namedtuple
City = namedtuple('City','cidade estado pais populacao')
print(City)
porto_alegre = City('Porto Alegre','RS','Brasil',1_000_000)
print(porto_alegre)
# Vamos imaginar que se deseje alterar a população de Porto Alegre. 
# Uma forma de se fazer isso é:
*diversas_caracteristicas,_ = porto_alegre
print(diversas_caracteristicas)
porto_alegre = City(*diversas_caracteristicas,1_500_000)
print(porto_alegre)

# Outra possibilidade é, a partir de uma lista, criar os novos valores e aplicar
# o método _make().
diversas_caracteristicas.append(1_600_000)
porto_alegre = City._make(diversas_caracteristicas)
print(porto_alegre)

# Há, no entanto, um caminho muito mais simples: a utilização do método '_replace'.
bento_goncalves = City('Bento Gonçalves', 'SC', 'BR', 50_000)
print(bento_goncalves)
# Vamos imaginar que se desejem alterar os campos 'estado' e 'populacao'. 
bento_goncalves = bento_goncalves._replace(estado='RS', populacao=100_000)
print(bento_goncalves)

# Se for do meu interesse criar uma classe que aproveita os atuais campos existentes
# em City e insere o campo 'regiao', então é possível se fazer o seguinte:
campos_novos = City._fields+('regiao',)
CityExt = namedtuple('CityExt',campos_novos)
print(CityExt._fields)
# É possível "aproveitar" valores existentes. 
bento_ext = bento_goncalves+('Serra',)
print(*bento_ext)
bento_completa = CityExt(*bento_ext)
print(*bento_completa)