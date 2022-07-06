'''
Aula 119. Closing Generators - Lecture
'''
def read_file(f_name):
    f = open(f_name)
    try:
        for row in f:
            # Retorna linha por linha.
            yield row.strip("\n")
    finally:
        # Condições 
        f.close()
arquivo = read_file("file1.txt")
print(next(arquivo))
print(next(arquivo))
# Para fechar o arquivo, é possível se utilizar o método close(), que faz com que
# o que estiver dentro de finally, na definição do generator, seja executado, 
# independentemente do que estiver ocorrendo dentro de try.  
arquivo.close()

# O que ocorre de fato é que a exceção GeneratorExit é gerada, fazendo com que
# se saia de 'try'.
def read_file(f_name):
    f = open(f_name)
    try:
        for row in f:
            # Retorna linha por linha.
            yield row.strip("\n")
    except GeneratorExit:
        print('Generator close called.')
    finally:
        # Condições 
        f.close()
arquivo = read_file("file1.txt")
print(next(arquivo))
arquivo.close()


