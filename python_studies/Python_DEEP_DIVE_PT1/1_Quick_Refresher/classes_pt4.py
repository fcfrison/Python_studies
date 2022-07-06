# Forma mais pytohnica de implementar getters e setters.
class Retangulo:
    '''
    Cria a classe retângulo.
    '''
    def __init__(self,lado, altura):
    # Como self.lado chama o método @lado.setter lado(self,lado), que é um 
    # setter, então o que está ocorrendo é que para registrar o atributo
    # 'lado', o usuário deverá obedecer a condição lado>0. Ou seja, não é 
    # possível se acessar o atributo diretamente. 
        self.lado = lado
        self.altura = altura
    
    @property
    def lado(self):
        '''
        Esse método implementa o getter do atributo 'lado'.
        '''
        # O decorator faz com que ao se fazer self.lado, esteja a se chamar
        # o método lado(self).
        return self.lado
    
    @lado.setter
    def lado(self,lado):
        '''
        Esse método implementa o setter do atributo 'lado'.
        '''
        # O decorator faz com que esse método, apesar de possuir o mesmo nome
        # do criado acima, seja diferente e mais faz com que o Python saiba
        # que se está tratando de alterar valores do atributo 'lado'.
        if lado<=0:
            raise ValueError('O lado deve ser positivo.')
        else:
            self.lado = lado

    @property
    def altura(self):
        '''
        Esse método implementa o getter do atributo 'altura'.
        '''
        return self._altura

    @altura.setter
    def altura(self,altura):
        '''
        Esse método implementa o setter do atributo 'altura'.
        '''
        if altura<=0:
            raise ValueError('A altura deve ser positiva.')
        else:
            self._altura = altura

    def __str__(self):
        '''
        Representação em string do objeto.
        '''
        return f'Retângulo de altura {self.altura} e de lado {self.lado}'
    
    def __repr__(self):
        '''
        Representação do objeto no console. 
        '''
        return f'Retangulo({self.lado},{self.altura})'
    
    def __eq__(self, other):
        '''
        Método especial utilizado para comparar dois retângulos. 
        Dois retângulos serão iguais se os seus lados e as suas 
        alturas forem iguais. 
        '''
        if isinstance(other,Retangulo):
        # Se o objeto other for da classe Retangulo, então 
        # isinstance(other,Retangulo)==True. Logo, a comparação é possível.
            return self.altura==other.altura and self.lado==other.lado
        else:
            return False

    def __lt__(self,other):
        '''
        Método especial utilizado para realizar comparações do tido 
        self.algum_critehrio < other.algum_critehrio
        '''
        if isinstance(other,Retangulo):
        # É preciso garantir que ambos os objetos podem ser comparados.
            return self.area() < other.area()
        else:
            return NotImplemented

retangulo_1=Retangulo(-50,35)
# Chamando o método @property lado(self) --> utilizando um getter.
retangulo_1.lado

# Chamando o método @altura.setter altura(self,altura)
retangulo_1.altura=40