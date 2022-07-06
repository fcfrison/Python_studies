'''
44. Python's Built-In Iterables and Iterators
'''
# Há funções/classes intrínsecas ao Python que retornam iteradores e iteráveis.
# Todos os iteráveis ou iteradores intrínsecos são 'lazy'. Ou seja, a iteração só 
# ocorre no momento em que for se iterar sobre eles. 
r = range(10)
# range retorna um iterável (ou seja, ela não contém __next__ implementado
# nela, mas contém o método __iter__).
print(r)

# Já a função zip retorna um iterador. 
z = zip([1,2,3],'abc')
print(z)

# Outro iterador notável é a função 'open'. Sendo um 'lazy iterator', a iteração
# só será realizada quando algo como um 'for' loop for chamado.  
with open('cars.csv') as file:
    # O rótulo 'file' aponta para o endereço de memória do iterador 'open'. 
    # No caso abaixo, todo o arquivo foi lido e convertido em uma lista. 
    l = file.readlines()
print(l)

# Vamos imaginar que exista o desejo de se ler linha por linha e escolher determinadas
# informações. Ao se fazer o que está abaixo, não há a necessidade de se carregar todo 
# o documento 'cars.csv' na memória, apenas a informação desejada.  
origins = set()
with open('cars.csv') as file:
    # Pulando as duas primeiras linhas. 
    next(file)
    next(file)
    for row in file:
        origin = row.strip('\n').split(';')[-1]
        origins.add(origin)

