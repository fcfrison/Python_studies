# Um cuidado que é necessário ao se trabalhar com parâmetros que tenham 
# valores default está ligado à questão de se instanciar objetos. 

from datetime import datetime

def func_1(mensagem, dt = datetime.utcnow()):
    '''
    Ao se instanciar datetime.utcnow(), se faz com que 'dt' aponte para o 
    endereço de memória de datetime.utcnow(). Porém, esse valor é gerado apenas
    no momento em que as variáveis 'func_1' e 'dt' são criadas (o que ocorre
    antes inclusive de se chamar a função pela primeira vez). Assim sendo, ao 
    se utilizar o valor default para 'dt', não se estará gerando novos valores 
    de tempo. 
    '''
    print(f'mensagem = {mensagem}, time = {dt}')

func_1('mensagem 1')
func_1('mensagem 2')


def func_2(mensagem, dt = None):
    '''
    Para resolver o problema de func_1, basta atribuir None para 'dt', tornando 
    esse parâmetro opcional para o usuário da função e implementar o que segue 
    abaixo.
    '''
    if not dt:
        dt = datetime.utcnow()
    print(f'mensagem = {mensagem}, time = {dt}')

func_2('mensagem 3')
func_2('mensagem 4')

# Um problema semelhante ao apontado acima ocorre quando se trabalha com tipos
# mutáveis (listas, dicionários, conjuntos, etc.)

def func_3(name, quantity, unit, grocery_list=[]):
    '''
    A ideia é que essa função crie uma lista, caso a lista não tenha sido passada
    como argumento, e se retorne a mesma com os valores passados como argumentos. 
    Ao se fazer 'grocery_list=[]', antes mesmo da função ser chamada, é alocado 
    um espaço de memória para '[]' e aponta-se 'grocery_list' para o mesmo. Assim,
    toda a vez que não for especificado uma lista na chamada de 'func_3', não 
    estará a se criar uma lista nova, mas, sim, a se anexar os itens à primeira
    lista criada. 
    '''
    grocery_list.append((name,quantity,unit))
    print(grocery_list)
    return grocery_list

lista_1 = func_3('notebook', 1, 'R$')
lista_2 = func_3('toalha', 100, 'R$')

# A solução para o problema é fazer 'grocery_list=None' como o valor padrão.
def func_4(name, quantity, unit, grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append((name,quantity,unit))
    print(grocery_list)
    return grocery_list

lista_3 = func_4('notebook', 1, 'R$')
lista_4 = func_4('toalha', 100, 'R$')
