'''
Aula 22. Custom Sequences - Part 2A - Coding
'''
# Para implementar uma sequência customizada, é preciso atentar a diversos 
# métodos especiais. 
# Os símbolos '+'  e '=+' são implementados através dos métodos especiais 
# __add__ e __iadd__.
class MyClass:
    def __init__(self, name:str) -> None:
        self.name = name
    def __repr__(self) -> str:
        return f"MyClass({self.name})"
    def __add__(self,other):
        '''
        Método que implementa self + other. Por definição, ao se utilizar esse
        método, um novo endereço de memória será gerado.
        '''
        return MyClass(self.name + other.name)
    def __iadd__(self,other):
        '''
        Método que implementa self += other. Por definição, ao se utilizar este 
        método, não será gerado um novo endereço de memória.
        '''
        if isinstance(other,MyClass):
            self.name+=other.name
        else:
            self.name+=other
        return self
    def __mult__(self,n:int):
        '''
        Método que implementa self*n. Por definição, ao se utilizar este 
        método, será gerado um novo endereço de memória.
        '''
        if isinstance(n,int):
            return MyClass(self.name*n)
        else:
            raise TypeError
    def __rmult__(self,n:int):
        '''
        Método que implementa n*self. Por definição, ao se utilizar este 
        método, será gerado um novo endereço de memória.
        A diferença em relação a __mult__ é que o inteiro estará à direita
        da sequência.
        '''
        return self.__mult__(n)
    def __imult__(self,n:int):
        '''
        Método que implementa self*=n. Por definição, ao se utilizar este 
        método, não será gerado um novo endereço de memória.
        '''
        if isinstance(n,int):
            self.name*=n
            return self
        else:
            raise TypeError
    def __contains__(self,value):
        '''
        Método que implementa o operador 'in'. Ou seja, verifica se determinado
        valor está na sequência.
        '''
        return value in self.name
    


c1 = MyClass("Felipe")
c2 = MyClass("Daiana")
print(f'id(c1) = {id(c1)}, id(c2) = {id(c2)}')
concatena = c1 + c2
print(f'{concatena}, id(concatena) = {id(concatena)}') 
c1+=c2
print(f'{c1}, id(c1) = {id(c1)}') 
