# O operador '**kwargs', definido como o parâmetro de uma função, captura quaisquer
# argumentos nomeados passados "restantes" em um dicionário.
# Na função abaixo, não serão aceitos argumentos posicionais, sendo mandatório
# que se passe um argumento nomeado para o parâmetro 'a' e eventuais argumentos
# nomeados excedentes serão incorporados em 'kwargs' como um par key:value.


def func_1(*,a,**kwargs):
    print(a, kwargs)

func_1(a=25,b=True, c=list(range(0,3)))

def func_2(**kwargs):
    '''
    Essa função aceita apenas argumentos nomeados, porém sem especificar nenhum
    como mandatório.
    '''
    print(kwargs)
func_2(a=25, b=25.6965)

def func_3(*args, **kwargs):
    '''
    Essa função aceita uma quantidade indefinida de argumentos posicionais, 
    bem como uma quantidade indefinida de argumentos nomeados. Os argumentos
    posicionais serão inseridos na tupla 'args' e os nomeados no dicionário
    'kwargs'.
    '''
    print(args, kwargs)

func_3(6,'felipe',True, a=4, b=None)

def func_4(a,b,*,sentence,**kwargs):
    '''
    Essa função aceita dois argumentos posicionais e infinitos argumentos nomeados.
    '''
    print(a,b,sentence,kwargs)

func_4(6,'felipe',sentence=True, c=4, d=None)
