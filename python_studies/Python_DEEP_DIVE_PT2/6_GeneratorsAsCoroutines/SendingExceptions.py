'''
121. Sending Exceptions to Generators - Lecture
'''
import inspect
# É possível, em um algoritmo, fazer com que uma exceção qualquer seja jogada
# para o 'generator', que pode, por exemplo, tratar essa exceção e continuar
# o seu fluxo. Ou seja, nem toda a exceção levantada irá, necessariamente, fazer
# c/q o programa seja interrompido.
# 1ª situação: o generator não trata o erro e é encerrado. 
def gen():
    try:
        while True:
            received = yield
            print(f'Valor {received} recebido.')
    except ValueError:
        print('um ValueError foi recebido')
    finally:
        # Como o erro foi tratado, o 'finally' será executado, um return 
        # ocorrerá e uma StopIteration será "levantada" (e ñ ValueError.)
        print("Uma exceção ocorreu.")

g=gen()
next(g)
g.send('olá')
# Verificando o estado do generator.
print(inspect.getgeneratorstate(g))
#print(g.throw(ValueError))
#print(inspect.getgeneratorstate(g))


# Vamos imaginar que, ao ocorrer um erro, ñ se deseje fechar o generator, mas 
# tratar a exceção e fazer com que o generator fique no estado suspended. 

def gen_():
    while True:
        try:
            received = yield
            print(received)
        except ValueError as ex:
            print('Value error received',str(ex))
g1 = gen_()
next(g1)
g1.send("olá")
g1.throw(ValueError,"Deu ruim")

# O controle do envio de informações a um banco de dados pode ser efetuado através
# do envio de sinais um esse generator através de exceções.
# Nessas situações, as exceções ñ são utilizadas no sentido de ter ocorrido um erro, 
# mas de controlar o fluxo. 
class CommitException(Exception):
    '''
    Exceção que informa ao generator que é possível se realizar um commit.
    '''
    pass

class RollbackException(Exception):
    '''
    Exceção que informa ao generator que um roolback deve ser realizado commit.
    '''
    pass

def write_to_bd():
    print('abrindo uma conexão com o banco de dados')
    print('iniciando um conexão')
    try:
        while True:
            try:
                # Recebendo os dados que serão enviados ao banco de dados. 
                data = yield
                print("Carregando dados no banco de dados", data)
            except CommitException:
                print('comitando a transação')
                print('abrindo uma nova transação')
            except RollbackException:
                print('abortando a transação')
                print('abrindo uma nova transação')
    finally:
        # Qualquer exceção que não seja CommitException ou RollbackException
        # fará com que o código chegue aqui.
        print('fechando o generator...')
        print('abortando a transação...')
        print('fechando a conexão com o banco de dados...')

# Transação 1 com o banco de dados.
sql = write_to_bd()
# Iniciando o generator.
next(sql)
sql.send('dados 1')
# Comitando os dados.
sql.throw(CommitException)

# Ocorrendo outra exceção, ela será levada ao 'caller' e o generator fechado. 
sql.throw(ValueError)
print(inspect.getgeneratorstate(sql))

# Transação 2 com o banco de dados.
sql_1 = write_to_bd()
# Iniciando o generator.
next(sql_1)
sql_1.send('dados 1')
# Comitando os dados.
sql_1.throw(CommitException)
sql_1.close()
print(inspect.getgeneratorstate(sql_1))