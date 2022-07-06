# É possível se retornar uma 'namedtuple', ao invés de uma simples 'tuple',
# a partir de uma função. A vantagem disso é que a leitura do código é facilitada, 
# uma vez que as ferramentas de leitura de IDEs como o VsCode lêem melhor o código.
from collections import namedtuple
from random import randint, random
from re import A

Color = namedtuple('Color','red green blue alpha')

def random_color():
    red = randint(0,255)
    blue = randint(0,255)
    green = randint(0,255)
    alpha = round(random(),2)
    return Color(red,blue,green,alpha)