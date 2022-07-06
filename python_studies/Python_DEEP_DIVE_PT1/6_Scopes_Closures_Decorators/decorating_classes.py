# É possível se criar na execução do programa métodos e atributos a 
# classes e métodos definidos built-in.
from fractions import Fraction

from pytz import timezone
# Definindo o método 'speak' na classe 'Fraction'. 
Fraction.speak = lambda self, message: print('Fraction disse {0}'.format(message))
f = Fraction(2,3)
f.speak('Hello world!!')

# Utilizando uma função para criar um método em uma classe. 
from fractions import Fraction
def dec_speak(classe):
    classe.speak = lambda self, mensagem: '{0} says: {1}'.format(
        self.__class__.__name__, mensagem
    )
    return classe

Fraction = dec_speak(Fraction)

# Criando uma função que retorna informações sobre uma instância de uma classe. 
# A ideia é criar um log para uma classe qualquer. 
from datetime import datetime, timezone
def info(self):
    '''
    Como 'info' foi pensado como um método, ou seja, uma função que está dentro 
    de uma classe, é natural que, no mínimo, o primeiro argumento seja o endereço 
    da instância.
    '''
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('Class: {0}'.format(self.__class__.__name__))
    results.append('id: {0}'.format(hex(id(self))))
    for keys,values in vars(self).items():
        results.append('{0}: {1}'.format(keys,values))
    return results

def debug_info(classe):
    '''
    Função que insere na classe passada como argumento um método.
    '''
    classe.debug = info
    return classe

class Person:
    def __init__(self, nome, ano_de_nascimento):
        self.nome = nome
        self.ano_de_nascimento = ano_de_nascimento

    def say_hi():
        return "Olá mundo!!" 

Person = debug_info(Person)
pessoa_1 =Person('Felipe',1987)
pessoa_1.debug() 

# Outra forma de decorar a função é:
@debug_info
class Person_:
    def __init__(self, nome, ano_de_nascimento):
        self.nome = nome
        self.ano_de_nascimento = ano_de_nascimento

    def say_hi():
        return "Olá mundo!!" 

pessoa_2 = Person_('Daiana',1991)
pessoa_2.debug()


# Outro exemplo. 
@debug_info
class Automobile:
    def __init__(self,fabricante,modelo,ano,vel_max):
        self.fabricante = fabricante
        self.modelo = modelo
        self.ano = ano
        self.vel_max = vel_max
        self._vel = 0 
    
    @property
    def vel(self):
        return self._vel
    
    @vel.setter
    def vel(self,nova_vel):
        if nova_vel>self.vel_max:
            return ValueError('A nova velocidade não pode exceder a vel_max.')
        else:
            self._vel = nova_vel


automovel_1 = Automobile('Renault','Kwid',2020,120)
automovel_1.vel = 50
automovel_1.debug()

# Outro exemplo. Na classe abaixo, foram implementados os métodos que permitem
# checar a igualdade entre dois pontos e verificar se um ponto é menor do que o 
# outro. Para implementar as demais comparações (maior, maior ou igual, menor ou
# igual), se utilizará um decorator criado em 'functools'.
#  
from math import sqrt
from functools import total_ordering

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __abs__(self):
        '''
        Método especial para implementar o valor absoluto.
        '''
        return sqrt(self.x**2+self.y**2)
    
    def __repr__(self):
        '''
        Método especial para reprodução da classe no terminal.
        '''
        return f'{self.__class__.__name__} ({self.x},{self.y})'
    
    def __eq__(self,other):
        '''
        Método especial para checar a igualdade entre dois pontos.
        '''
        if isinstance(other,Point):
            return self.x ==other.x and self.y == other.y
        else:
            False
    
    def __lt__(self,other):
        '''
        Método especial que compara se self<other.
        '''
        if isinstance(other,Point):
            return abs(self)<abs(other)
        else:
            return NotImplementedError
# Implementando o decorator debug_info
Point = debug_info(Point)
Point = total_ordering(Point)
ponto_1 = Point(5,5)
ponto_2 = Point(10,5)
ponto_3 = Point(5,5)
print(ponto_1==ponto_3)
print(ponto_1<ponto_3)
print(ponto_1<=ponto_3)