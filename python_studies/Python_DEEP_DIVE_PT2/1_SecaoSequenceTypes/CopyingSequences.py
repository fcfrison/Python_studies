'''
Aula 11. Copying Sequences - Lecture
'''
# É uma boa prática de programação retornar valores, a partir de uma função, se 
# esses valores forem novos espaços de memória. Do contrário, é interessante que
# a função não retorne nada. 
def reverse_(l:list)->list:
    '''
    Função que reverte uma lista, alocando novo espaço de memória. 
    '''
    nova_lista = l.copy()
    nova_lista.reverse()
    print(nova_lista)
    return nova_lista

lista = list(range(10))
print(id(lista))
nova_lista = reverse_(lista)
print(nova_lista)
print(id(nova_lista))

def reverse_s_alocar(l:list)->None:
    '''
    Função que reverte uma lista, sem alocar novo espaço de memória. 
    '''
    l.reverse()
reverse_s_alocar(nova_lista)
print(nova_lista)
print(id(nova_lista))

# Um cuidado a se tomar com o método copy() é que é alocado um novo
# endereço de memória para a estrutura que contém os elementos, por
# exemplo, a lista, mas os elementos do novo objeto continuam apontado 
# para os endereços dos antigos. 
lista_x = list(range(3))
lista_x_copy = lista_x.copy()
print(id(lista_x))
print(id(lista_x_copy))
print(id(lista_x[0]))
print(id(lista_x_copy[0]))
# Isso não é um problema quando os elementos forem imutáveis, como no caso acima. 
# Porém, isso é um problema quando os elementos forem mutáveis (uma lista cujos 
# elementos são listas, por exemplo).
lista_x_copy[0] = 50
print(lista_x)
print(lista_x_copy)
# O problema é esse:
lista_1 = [[1,2],[3,4],[5,6]]
lista_2 = lista_1.copy()
# Ao se alterar o elemento da lista sem alterar o seu endereço, como ocorre com o 
# o método 'append', altera-se o valor de qualquer rótulo que aponte para ele. 
lista_2[0].append([None,None,None])
print(lista_1)
print(lista_2)

# Para evitar esse tipo de problema com objetos que possuem elementos mutáveis, 
# é importante se utilizar o módulo 'copy', que possui a função 'deepcopy'. 
from copy import deepcopy, copy
import pandas as pd
dict_ = [
    {'Coluna 1':1, 'Coluna 2':10,'Coluna 3':20},
    {'Coluna 1':2, 'Coluna 2':11,'Coluna 3':21},
    {'Coluna 1':3, 'Coluna 2':12,'Coluna 3':22},
    {'Coluna 1':4, 'Coluna 2':13,'Coluna 3':23},
    {'Coluna 1':5, 'Coluna 2':14,'Coluna 3':24},
]
df = pd.DataFrame(dict_)
print(df.to_string())
# Efetuando uma deepcopy.
df_deep_copy = deepcopy(df)
print(df_deep_copy.to_string())

# O deepcopy funciona para quaisquer objetos. 
class Point:
    '''
    Classe ponto: representação de um ponto.
    '''
    def __init__(self,x:float,y:float):
        '''
        Parâmetros
        -----------
            x: float
                Coordenada x do ponto.
            y: float
                Coordenada y do ponto.
        '''
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Point({self.x},{self.y})'

class Line:
    '''
    Classe linha: representação de uma linha.
    '''
    def __init__(self,p1:Point, p2:Point):
        '''
        Parâmetros
        -----------
            p1: Point
                Instância da classe Ponto.
            p2: Point
                Instância da classe Ponto.
        '''
        self.p1 = p1
        self.p2 = p2
    def __repr__(self):
        return f'Line({self.p1.__repr__},{self.p2.__repr__})'

p1 = Point(1,1)
p2 = Point(2,2)
linha_1 = Line(p1,p2)
linha_2 = deepcopy(linha_1)
linha_3 = copy(linha_1)
# Dentro de 'linha_1', os atributos 'p1' e 'p2' são mutáveis, afinal de contas, 
# "dentro" deles há outros atributos, que possuem endereços de memória próprios e
# que podem ser alterados sem que o endereço da instância seja alterada. 
# Ao fazer uma deepcopy de linha_1, são feitas cópias também das instâncias 'p1'
# e 'p2'. 
print(f'id original--> {id(linha_1.p1)}')
print(f'deep copy->id = {id(linha_2.p1)}')
print(f'shallow copy-->id = {id(linha_3.p1)}')


print(id(linha_1.p1))
print(id(linha_2.p1))