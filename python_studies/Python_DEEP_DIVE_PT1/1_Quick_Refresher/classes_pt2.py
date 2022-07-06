# Continuação do código da parte 1. Utilização de 'getters' e 'setters'.
class Retangulo:
    '''
    Cria a classe retângulo.
    '''
    def __init__(self,lado, altura):
        # self._lado indica que essa é, por convenção, uma variável privada,
        # que não deve ser acessada diretamente, embora seja possível acessá-la
        # diretamente.  
        self._lado = lado
        self._altura = altura
    
    def get_lado(self):
        '''
        Método criado para que o usuário da classe possa acessar o valor
        do atributo _lado.
        '''
        return self._lado
    
    def set_lado(self,lado):
        '''
        Método criado para que o usuário da classe possa alterar o valor 
        do atributo _lado. 
        '''
        if lado <=0:
            raise ValueError('O valor deve ser positivo.')
        else:
            self.l_lado = lado

    def __str__(self):
        '''
        Representação em string do objeto.
        '''
        return f'Retângulo de altura {self._altura} e de lado {self._lado}'
    
    def __repr__(self):
        '''
        Representação do objeto no console. 
        '''
        return f'Retangulo({self._lado},{self._altura})'
    
    def __eq__(self, other):
        '''
        Método especial utilizado para comparar dois retângulos. 
        Dois retângulos serão iguais se os seus lados e as suas 
        alturas forem iguais. 
        '''
        if isinstance(other,Retangulo):
        # Se o objeto other for da classe Retangulo, então 
        # isinstance(other,Retangulo)==True. Logo, a comparação é possível.
            return self._altura==other._altura and self._lado==other._lado
        else:
            return False

retangulo_1=Retangulo(50,35)

# A forma correta de se verificar o atributo 'lado' é através deste método. 
retangulo_1.get_lado()

# A forma correta de se setar um novo valor para o atributo 'lado' é através 
# deste método.
retangulo_1.set_lado(45)