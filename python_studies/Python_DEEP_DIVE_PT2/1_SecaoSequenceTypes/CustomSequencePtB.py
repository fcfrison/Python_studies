'''
Aula 23. Custom Sequences - Part 2B
'''
# Será construída uma sequência que representa os pontos de um polígono. 
# Por definição, todos os pontos gerados devem ser numéricos. 
import numbers

class Point:
    '''
    Classe que representa um ponto.
    '''
    def __init__(self,x:numbers.Real, y:numbers.Real):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x,y)
        else:
            raise TypeError('As coordenadas do ponto devem ser números reais.')

    def __repr__(self)->str:
        '''
        Método especial de representação da classe Point.
        '''
        return f'Point(x = {self._pt[0]}, y = {self._pt[1]})'
    
    def __len__(self):
        '''
        Método especial para especial o tamanho da sequência.
        '''
        return len(self._pt)
    
    def __getitem__(self,s):
        '''
        Método especial para capturar elementos da sequência. A partir da 
        implementação desse método é possível desempacotar a tupla.
        ''' 
        return self._pt[s]
p1 = Point(10,5)
# Ao se desempacotar (da maneira como está sendo feito abaixo), a linguagem
# de programação está a chamar o método especial __getitem__, passando como
# argumento os valores s=0, s=1 e s=2.
x,y = p1

class Polygon:
    def __init__(self,*pts):
        if pts:
            self._pts = [Point(*pt) for pt in pts]
        else:
            self._pts = []
    def __repr__(self):
        pts_str = ', '.join([str(pt) for pt in self._pts])
        return f'Polygon({pts_str})'
    def __len__(self):
        return len(self._pts)
    def __getitem__(self,s):
        return self._pts[s]
    def __setitem__(self,s,valor):
        if isinstance(s,int):
            self._pts[s] = Point(*valor)
        else:
            self._pts = [Point(*item) for item in valor]
    def __add__(self,other):
        '''
        O método especial __add__ é responsável por criar uma nova instância
        da classe Polygon, concatenando os pontos de dois polígonos. 
        '''
        if isinstance(other,Polygon):
            return Polygon(*self._pts,*other._pts)
        else:
            raise TypeError("Só é possível realizar a concatenação com outros polígonos.")
    def __iadd__(self,other):
        '''
        Método especial por realizar concatenação 'in-place', ou seja, sem alocar
        novos espaços de memória.
        '''
        if isinstance(other,Polygon):
            points = other._pts
        else:
            # Se não for um objeto da classe Polygon, então se tentará iterar
            # sobre o objeto 'other' e, a partir dos seus elementos, gerar 
            # novos pontos. 
            points = [Point(*item) for item in other]
        self._pts = self._pts + points
        return self
    def append(self,pt):
        '''
        Método para anexar novos pontos ao polígono.
        '''
        self._pts.append(Point(*pt))
    def insert(self,pt):
        '''
        Método para inserir novos pontos no polígono.
        '''
        self._pt.insert(Point(*pt))
    def extend(self,pts):
        '''
        Método extender os pontos de um polígono.
        '''
        if isinstance(pts,Polygon):
            self._pts+=pts._pts
        else:
            points = [Point(*item) for item in pts]
            self._pts+=points
    def __delitem__(self,s):
        '''
        Método especial para deletar itens.
        '''
        del self._pts[s]
    def pop(self,i):
        '''
        Método para remover um item específico na posição 'i' da sequência.
        '''
        return self._pts.pop(i)
    def clear(self):
        '''
        Método para limpar a lista, ou seja, remover todos os elementos da 
        lista.
        '''
        self._pts.clear()







pol1= Polygon([1,2],Point(3,4))
pol2= Polygon([5,6],[7,8])
# Realizando uma concatenação 'in-place'.
pol1+=pol2
print(pol1)

pol3 = Polygon((1,0),(2,0),(5,5,))
pol3[0] = Point(0,0)
    
