'''
Aula 120. Closing Generators - Coding
'''
# É possível se interromper a execução de um generator através da utilização 
# do método close.
import csv
def parse_file(f_name):
    print("Abrindo o arquivo.")
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        reader = csv.reader(f, dialect=dialect) 
        for row in reader:
            yield row
    finally:
        print("Fechando o arquivo.")
        f.close()
import itertools
parser = parse_file('cars.csv')
for row in itertools.islice(parser,10):
    print(row)
# Para "fechar" o generator, basta interromper a execução do try e "pular" para
# o "finally", o que pode ser feito através do método close. 
parser.close()

def parse_file(f_name):
    print("Abrindo o arquivo.")
    f = open(f_name, 'r')
    try:
        dialect = csv.Sniffer().sniff(f.read(2000))
        f.seek(0)
        next(f)
        reader = csv.reader(f, dialect=dialect) 
        for row in reader:
            try:
                yield row
            except GeneratorExit:
                print('ignoring call to close generator.')
                # Ao declarar 'return' dentro de um generator, uma exceção do 
                # tipo StopIteration é levantada, a ql é tratada e silenciada
                # pelo interpretador do Python, o que faz c/q 'finally' seja 
                # executada. 
                return
    finally:
        print("Fechando o arquivo.")
        f.close()
import itertools
parser = parse_file('cars.csv')
for row in itertools.islice(parser,3):
    print(row)
# Para "fechar" o generator, basta interromper a execução do try e "pular" para
# o finally, o que pode ser feito através do método close. 
parser.close()


# A partir da utilização de um generator como coroutine, é possível fazer transações
# com uma base de dados. 
def save_to_db():
    print('starting new transaction.')
    while True:
        try:
            # Enviando dados à base de dados. 
            data = yield
            print('sending data to the database.',data)
        except Exception:
            # Se algum tipo de exceção q ñ seja uma GeneratorExit ocorrer, então
            # a transação será abortada.
            print('aborting transaction')
        except GeneratorExit:
            # Assim que close for chamado a partir de um generator, uma exceção 
            # do tipo GeneratorExit será levantada. 
            print('committing the transaction')
            raise GeneratorExit
        
connection = save_to_db()
connection.send('linha 1')
connection.send('linha 2')
# levantando uma exceção que não seja GeneratorExit.
connection.send(eval('1/0'))

def save_to_db():
    print('starting new transaction')
    # flag que indica se uma exceção ocorreu ou não.
    is_abort = False
    try:
        while True:
            data = yield
            print(f'Enviando {data} para a base de dados.')
    except Exception:
        # Se uma exceção ocorrer.
        is_abort = True
        raise Exception
    finally:
        if is_abort:
            print("Roolback transaction")
        else:
            print("Commit transaction")
        print("Fecha a conexão com o banco de dados.")
