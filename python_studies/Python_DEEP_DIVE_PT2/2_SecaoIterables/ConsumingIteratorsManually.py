'''
39. Example 1 - Consuming Iterators Manually
'''
# É possível se utilizar da distinção entre objeto iterável e objeto iterador 
# para realizar a seleção de dados em arquivos, por exemplo.
import collections

def cast(data_type:list, value):
    '''
    Converte os valores passados como argumentos para tipos específicos.
    '''
    if data_type =='DOUBLE':
     return float(value)
    if data_type == 'INT':
        return int(value)
    else:
        return str(value)

def cast_row(data_types:list, data_row:list)->list:
    '''
    Função que recebe uma linha em formato de lista, formata tais os itens da lista
    para determinados tipos de dados e retorna uma lista formatada.
    '''
    return [cast(data_type,value) for data_type, value in zip(data_types, data_row)]

# O arquivo 'cars.csv' possui na primeira linha o nome das colunas, na segunda linha
# o tipo de dado da coluna e nas demais linhas os valores da tabela. 
cars = []
with open('cars.csv') as file:
    # Como 'file' é um arquivo iterável, é possível se chamar o objeto que se 
    # encontra em __iter__. Ou seja, é possível se criar uma instância do seu
    # iterador e registrar o seu valor na memória. 
    file_iter = iter(file)
    # É possível se capturar diretamente a primeira linha do arquivo de texto.
    headers = next(file_iter).strip('\n').split(';')
    Car = collections.namedtuple('Car',headers)
    # Após ter chamado o método especial 'next', é possível se avançar para a 
    # segunda linha, que nesse caso contém os tipos de dados associados às colunas. 
    data_types = next(file_iter).strip('\n').split(';')
    # Após ter se passado "manualmente" as duas primeiras linhas do arquivo de
    # texto, é possível se iterar nas demais linhas. 
    for line in file_iter:
        data = line.strip('\n').split(';')
        data = cast_row(data_types,data)
        car = Car(*data)
        cars.append(car)
print(cars)