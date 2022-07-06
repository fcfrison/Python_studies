# É possível se estabelecerem valores default para as namedtuples.
from collections import namedtuple
Vector2D  = namedtuple('Vector2D','x1 y1 x2 y2 origin_x origin_y')
# Para se estabelecer valores padrão, é preciso se criar um protótipo.
vector_zero = Vector2D(x1=0,y1=0,x2=0,y2=0,origin_x=0,origin_y=0)
# Para se construirem novas instâncias de Vector2D, se utilizará 'vector_zero' 
# como modelo. 
vector_one = vector_zero._replace(x1=10,y1=10,x2=20,y2=20)
print(*vector_one)

# Outra abordagem é __defaults__.Em funções, a utilização é a seguinte:
def localizacao(x,y,z): 
    return x,y,z
# É possível se estabelecerem os valores default dessa forma.
localizacao.__defaults__=(0,0)
print(localizacao(10))

# Para a 'namedtuple', a coisa funciona assim:
Vector3D  = namedtuple('Vector3D','x1 y1 z1 x2 y2 z2 origin_x origin_y origin_z')
Vector3D.__new__.__defaults__ = 0,0,0
vector_two = Vector3D(10,10,10,10,10,10)
print(*vector_two)