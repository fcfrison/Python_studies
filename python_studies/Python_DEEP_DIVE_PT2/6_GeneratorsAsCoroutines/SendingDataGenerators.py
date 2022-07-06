'''
Aula 117. Sending to Generators - Lecture
'''
# É possível se enviar dados a um generator através de um yield.
def gen_echo():
    # yield está sendo utilizado para receber dados e ñ para enviar dados.
    while True:
        valor_recebido = yield "Alfredo", 3
        print(f'Foi recebido o valor: {valor_recebido}')
# Cria uma instância de gen_echo()
try:
    echo = gen_echo()
    # Fazendo com que o programa avance até o lado esquerdo da igualdade valor_recebido = yield.
    print(next(echo))
    print(next(echo))
    print(next(echo))
    print(next(echo))
    # Enviando um valor para o generator.
    print(echo.send('Felipe'))
    print(echo.send('Daiana'))
    next(echo)
    
except StopIteration:
    pass

# yield pode ser utilizado com dupla função: enviar um valor e receber um valor.
def squares(n:int):
    for i in range(n):
        # yield primeiro retornará o valor i**2 e, em seguida, receberá um 
        # valor e o atribuirá para o rótulo 'valor_recebido'.
        valor_recebido = yield i**2
        print(valor_recebido)
gen = squares(5)
# Colocando o generator no estado suspenso. 
print(next(gen))
# Fazendo com que yield receba um valor, atribua a 'valor_recebido' e, após isso,
# valore 'i**2'.
print(gen.send('Felipe'))

# É possível se criar um generator para calcular a média de um conjunto de valores
# a partir da utilização do yield como algo que envia informação e retorna informação. 
def media_atual_func():
    total = 0
    contador = 0
    media_atual = 0
    while True:
        # Ao se utilizar 'yield media_atual', primeiro yield retorna o valor da média atual
        # e, após isso, recebe um valor.
        valor = yield media_atual
        contador+=1
        total +=valor
        media_atual = total/contador
gen = media_atual_func()
print(f'O valor inicial da média é: {next(gen)}')
# Lançando o valor inicial.
print(f'A média é {gen.send(5)}')
print(f'A média é {gen.send(6)}')
print(f'A média é {gen.send(7)}')
print(f'A média é {gen.send(8)}')

