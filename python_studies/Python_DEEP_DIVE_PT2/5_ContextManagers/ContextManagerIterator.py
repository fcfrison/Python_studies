'''
Aula 100. Not just a Context Manager
'''
# É possível a criação de um iterador que poderá se utilizado apenas dentro
# de um context manager. Ou seja, se implementarão ambos os protocolos:
# o do 'iterator' e o do 'context manager'. 
class DataIterator:
    def __init__(self,fname) -> None:
        self._fname = fname
        self._f = None
    # Implementando o protocolo do iterador.
    def __iter__(self):
        return self
    def __next__(self):
        row = next(self._f)
        return row.strip('\n').split(',')

    # Implementando o protocolo do context manager. 
    def __enter__(self):
        self._f = open(self._fname)
        return self
    def __exit__(self, exc_type, exc_value, exc_tb):
        # Se o arquivo não tiver sido fechado.
        if not self._f.closed:
            self._f.close()
        return False
with DataIterator('./nyc_parking_tickets_extract.csv') as file:
    for row in file:
        print(row)