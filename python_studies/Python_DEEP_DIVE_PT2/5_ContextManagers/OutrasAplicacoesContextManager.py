'''
102. Additional Uses - Coding
'''
# Context managers podem ter outras utilidades, além de abrir e fechar arquivos.
import time


class Timer:
    def __init__(self):
        self.elapsed = 0
    def __enter__(self):
        '''
        Método especial que faz com que uma rotina entre no context manager.
        '''
        self.start = time.perf_counter()
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.stop = time.perf_counter()
        self.elapsed = self.stop - self.start
        return False
with Timer() as timer:
    # Atrasando a execução dentro do 'with' por 1 segundo.
    time.sleep(1)
print(timer.elapsed)

# Utilizando um context manager para gravar texto em um arquivo. 
import sys
class OutToFile:
    def __init__(self, file_name):
        self.file_name = file_name
        self.current_stdout = sys.stdout
    def __enter__(self):
        # Abrindo um arquivo de texto para escrita.
        self._file = open(self.file_name,'w')
        # Alterando a saída padrão para o arquivo. 
        sys.stdout = self._file
    def __exit__(self, exc_type, exc_value, exc_tb):
        # Fazendo c/q a saída padrão retorne a ser o terminal. 
        sys.stdout = self.current_stdout
        # Fechando o arquivo.
        if not self._file.closed:
            self._file.close()
        # Caso ocorra algum erro, o programa poderá ser interrompido.
        return False
with OutToFile('./test.txt'):
    print("Felipe")
    print("Frison")
