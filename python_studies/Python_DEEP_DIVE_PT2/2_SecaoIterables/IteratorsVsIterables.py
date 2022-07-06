'''
37. Iterators and Iterables
'''
# É preciso se separar a estrutura de dados que armazena os objetos que serão 
# iterados do objeto que faz a iteração. A estrutura de dados se "preocupa" com
# os dados, já o objeto iterador se preocupa com a ação de iterar. 

class Cidades:
    '''
    Classe que representa uma estrutura de dados para armazenar os nomes das 
    cidades. 
    '''
    def __init__(self,cidades:list):
        self.cidades = cidades
    def __len__(self):
        return len(self.cidades)

class CidadesIterador:
    '''
    Classe que representa o iterador de objetos da classe cidade.
    '''
    def __init__(self, _cidades:Cidades):
        # self._cidades retém o endereço de memória do objeto a ser iterado.
        self._cidades = _cidades
        self.i = 0 # Estabelece o valor inicial
    def __next__(self):
        '''
        Método especial que promove a iteração. Esse método é chamado quando 
        a função next() é utilizada.
        '''
        if self.i>=self._cidades.__len__():
            raise StopIteration
        else:
            item = self._cidades.cidades[self.i]
            self.i+=1
            return item
    def __iter__(self):
        '''
        O método __iter__ é um método protocolar que informa ao interpretador do 
        Python que os ojbetos da classe são iteráveis. 
        '''
        return self
    def __repr__(self):
        return f'{self.i}'
cidades = Cidades(['Bento Gonçalves', 'Caxias do Sul', 'Porto Alegre', 'Farroupilha'])

# Imagine-se que se deseje iterar sobre os elementos de 'cidades'. O primeiro passo 
# é verificar se, de fato, CidadesIterador e um iterador (isso é feito através de __iter__) 
sq_iterator = iter(CidadesIterador(cidades))
# Se o método __iter__ tiver sido criado, então isso significa que o desenvolvedor 
# está informando ao interpretador que aquele objeto é um iterador. Por isso, 
# a referência de memória utilizada é aquela retornada pelo método especial __iter__. 
while True:
    try:
        item = sq_iterator.__next__()
        print(item)
    except StopIteration:
        break

# Mas ter que chamar o iterador explicitamente todas as vezes que se deseja iterar
# sobre o objeto iterável é algo um tanto quanto tedioso. Por isso, a melhor opção
# é chamar o método __iter__ a partir da classe que contém a estrutura de dados. 

class Cidades:
    '''
    Classe que representa uma estrutura de dados para armazenar os nomes das 
    cidades. 
    '''
    def __init__(self,cidades:list):
        self.cidades = cidades
    def __len__(self):
        return len(self.cidades)
    def __iter__(self):
        '''
        O método especial __iter__ da classe iterável 'Cidades' cria uma instância
        do objeto iterador 'CidadesIterador' a cada vez que se deseje iterar sobre
        os itens de 'Cidades'.
        Ao implementar __iter__, está a se "dizer para o Python" que Cidades pode
        ser iterada e que possui um objeto iterador. 
        '''
        return self.CidadesIterador(self)

    class CidadesIterador:
        '''
        Classe que representa o iterador de objetos da classe cidade.
        '''
        def __init__(self, _cidades:Cidades):
            # self._cidades retém o endereço de memória do objeto a ser iterado.
            self._cidades = _cidades
            self.i = 0 # Estabelece o valor inicial
        def __next__(self):
            '''
            Método especial que promove a iteração. Esse método é chamado quando 
            a função next() é utilizada.
            '''
            if self.i>=self._cidades.__len__():
                raise StopIteration
            else:
                item = self._cidades.cidades[self.i]
                self.i+=1
                return item
        def __iter__(self):
            '''
            O método __iter__ é um método protocolar que informa ao interpretador do 
            Python que os ojbetos da classe são iteráveis. 
            '''
            return self
        def __repr__(self):
            return f'{self.i}'

cidades = Cidades(['New York', 'Dallas', 'Houston', 'Paris', 'Rome'])
# 'under the hood', o que ocorre é o seguinte:
sq_iterator = cidades.__iter__()
while True:
    try:
        item = sq_iterator.__next__()
        print(item)
    except StopIteration:
        break
capitais = Cidades(['Porto Alegre', 'Florianópolis', 'São Paulo', 'Curitiba', 'Rio de Janeiro'])
for capital in capitais:
    print(capital)
