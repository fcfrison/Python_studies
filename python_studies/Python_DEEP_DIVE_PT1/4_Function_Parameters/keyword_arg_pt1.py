# É possível se obrigar que um dos argumentos seja passado como keyword. 
# Após *args, é mandatório que todos os argumentos passados sejam nomeados.
def somar(*args, a):
    total = sum(args) + a
    print(total)

somar(2,3,5,4,6,a=10)

# É possível se fazer com que todos os argumentos passados sejam nomeados. 
def multiplicar(*,a,b,c):
    multiplicacao = a*b*c
    print(multiplicacao)

multiplicar(a=8,c=5,b=3.9897854)

# Mais casos. 
def funcao_1(a,b=1,*args,d,e=True):
    print(f'a={a},b={b},args={args},d={d},e={e}')

funcao_1(1,2,9.99, 54.89, 68.9654, d='Felipe')

# No caso abaixo, apenas 2 argumentos posicionais são permitidos.  
def funcao_2(a,b=1,*,d,e=True):
    print(f'a={a},b={b},d={d},e={e}')

funcao_2(1,2,d='Felipe', e=False)

