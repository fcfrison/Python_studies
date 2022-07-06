from decimal import Decimal
from html import escape

def html_escape(arg):
    '''
    Função que recebe um objeto qualquer e retorna, caso exista algum caractere
    especial, aquele caractere no formato da linguagem html.
    '''
    return escape(str(arg))

def html_int(a:int)->str:
    '''
    Recebe um inteiro e formata-o para html.
    '''
    return '{0}(<i>{1}</i>'.format(a,str(hex(a)))

def html_real(a:float)->str:
    '''
    Recebe um float e formata-o para html.
    '''
    return '{0:2f}'.format(round(a,2))

def html_str(s:str)->str:
    return html_escape(s).replace('\n','<br/>\n')

def html_lst(l:list)->str:
    items = ['<li>{0}</li>'.format(htmlize(item) for item in l)]
    print(''.join(items))
    return '<ul>\n' + ''.join(items) + '<\n/ul>'

def html_dict(d):
    items = ('<li>{0}={1}</li>'.format(htmlize(key),htmlize(value))
                for key,value in d.items()
                )
    return '<ul>\n' + '\n'.join(items) + '\n</ul>'

def htmlize(arg):
    '''
    Função que, a partir da verificação do tipo de dado do argumento, escolhe 
    qual função, das funções criadas acima, é a mais adequada a ser chamada. 
    '''
    if isinstance(arg,int):
        return html_int(arg)
    elif isinstance(arg,float) or isinstance(arg,Decimal):
        return html_real(arg)
    elif isinstance(arg,str):
        return html_str(arg)
    elif isinstance(arg,list) or isinstance(arg,tuple):
        return html_lst(arg)
    elif isinstance(arg,dict):
        return html_dict(arg)
    else:
        return html_escape(arg)

# Testando a função acima.
htmlize(150)


# Uma forma mais simples de se escrever htmlize é a seguinte. 
def htmlize(arg):
    registry = {
        object : html_escape,
        int : html_int,
        float : html_real,
        Decimal : html_real,
        str : html_str,
        list : html_lst,
        tuple : html_lst,
        set : html_lst,
        dict : html_dict
    }
    fn = registry.get(type(arg), registry[object])
    return fn(arg)
print(htmlize([100,250]))
