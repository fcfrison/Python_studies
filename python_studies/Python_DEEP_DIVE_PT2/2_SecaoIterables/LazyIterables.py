import math


class Circle:
    def __init__(self,r:float):
        # Ao fazer self.radius, está a se chamar o setter de 'radius', passando
        # 'r' como parâmetro. Ou seja, 'self.radius =' é o que chama o método 
        # 'radius'. Isso é assim, pq 'radius' foi definido como uma propriedade. 
        # Em outras palavras, para ter um setter em Python, primeiro é preciso
        # se ter um getter.   
        self.radius = r
    
    @property
    def radius(self):
        '''
        Método getter da classe Circle para a propriedade 'radius'.
        '''
        return self._radius
    @radius.setter
    def radius(self,r):
        '''
        Método setter da classe Circle para a propriedades 'radius'.
        '''
        # Do jeito que essa classe está configurada, toda a vez que um círuclo for criado, 
        # será passado um valor para 'r' e, automaticamente, será calculado o valor da área.
        self._radius = r
        self.area = math.pi * (r**2)

c1 = Circle(1)
print(c1.radius)

##############################################################
########## Lazy evaluations em uma classe qualquer ###########
##############################################################

class Circle:
    def __init__(self,r:float):  
        self.radius = r
        self._area = None
    
    @property
    def radius(self):
        '''
        Método getter da classe Circle para a propriedade 'radius'.
        '''
        return self._radius
    @radius.setter
    def radius(self,r):
        '''
        Método setter da classe Circle para a propriedades 'radius'.
        '''
        self._radius = r
        self._area = None # Ao fazer isso, está a se garantir q td a vez q o raio for alterado, a área deverá,
                          # caso chamada, ser calculada novamente. 
    
    @property
    def area(self):
        '''
        Método getter da classe Circle para a propriedade 'area'.
        '''
        if self._area==None: # Se a area ainda não foi calculada, então ela deve ser cálculada.
            return math.pi * (self.radius**2)
        else:
            return self._area # Se a área já foi calculada, então ñ há pq calculá-la de novo.

##############################################################
########## Lazy evaluations em um objeto iterável  ###########
##############################################################
class Factorials:
    def __init__(self,lenght:int):
        self.lenght = lenght
    def __iter__(self):
        '''
        Esse método faz com que a classe Factorials seja um iterável. 
        '''
        return self.FactIter(self.lenght)
    class FactIter:
        def __init__(self, lenght):
            self.i = 0
            self.lenght = lenght
        def __iter__(self):
            '''
            Esse método especial faz c/q a subclasse FactIter seja um iterável.
            Se o método especial __next__ também estiver definido, então os objetos
            instanciados a partir dessa classe serão iteradores. 
            '''
            return self
        def __next__(self):
            if self.i>=self.lenght:
                raise StopIteration
            else:
                # Ao colocar o cálculo do fatorial aqui, está se fazendo com que, ainda que 
                # uma instância da classe Factorials seja criada, o cálculo, de fato, só será
                # efetuado quando o iterador for chamado. 
                result = math.factorial(self.i)
                self.i +=1
                return result
fatorial = Factorials(10)
list(fatorial)