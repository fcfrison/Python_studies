'''
Aula 99. Caveat when used with Lazy Iterators
'''
# A depender de como o context manager for utilizado, bugs poderão surgir. 
# Ao executar o que segue abaixo, será levantado um erro do tipo 
# ValueError: I/O operation on closed file., uma vez que, após retornar 
# o objeto csv.reader(...), o método especial __exit__ é chamado e ele 
# fecha o arquivo 'file'.
import csv
def read_data():
    with open('nyc_parking_tickets_extract.csv','r') as file:
        return csv.reader(file, delimiter = ',', quotechar='"')
data = read_data()
for row in data:
    print(row)

# Se a função for alterada conforme está abaixo, então não haverá problemas, 
# uma vez que, dentro de with, nunca se chegou a sair de 'with'. 
def read_data():
    with open('nyc_parking_tickets_extract.csv','r') as file:
        yield from csv.reader(file, delimiter = ',', quotechar='"')
data = read_data()
for row in data:
    print(row)
    
