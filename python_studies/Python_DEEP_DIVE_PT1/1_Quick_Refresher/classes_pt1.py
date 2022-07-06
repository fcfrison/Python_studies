# Criando uma classe qualquer.
class Retangulo:
    '''
    Cria a classe retângulo.
    '''
    def __init__(self,lado, altura):
        self.lado = lado
        self.altura = altura
    
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
    
    def area(self):
        '''
        Calcula a área de um retângulo.
        '''
        return self.lado*self.altura
    
    def perimetro(self):
        '''
        Calcula o perímetro de um retângulo.
        '''
        return 2*(self.lado+self.altura)

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


    

retangulo = Retangulo(10,5)
retangulo.area()

# O método str(retangulo) chamará o método __str__(self).
str(retangulo)

# Ao se chamar apenas o objeto, como ocorre na linha executada abaixo,
# o método especial __repr__(self) será chamado, se o programa estiver sendo
# excutado em modo iterativo.
retangulo

# Comparando dois retângulos.
retangulo_2 = Retangulo(10,5)
# Ao se comparar dois objetos da classe Retangulo, o metodo especial __eq__(self,other)
# é chamado.
retangulo==retangulo_2
# Porém, ao fazer retangulo is not retangulo_2 teremos outro tipo de comparação.
# Ou seja, o método __eq__(self,other) não é chamado.
retangulo is not retangulo_2

# O método __eq__(self,other) está preparado para lidar com objetos que sejam 
# de classes diferentes de Retangulo. 
retangulo==1

# O método __ls__(self,other) é chamado ao se realizar a operação abaixo.
retangulo < retangulo_2