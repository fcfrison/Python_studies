class Averager:
    '''
    Classe que insere elementos a uma lista e calcula a média dos valores.
    '''
    def __init__(self):
        self.numbers = []
    
    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total/count
av1 = Averager()
av1.add(5)
av1.add(6)
av1.add(7)


# É possível realizar operação semelhante através de uma "closure".
def averager():
    numbers = []
    def add(number):
        # 'numbers' é uma closure, já que não está no escopo local da função 'add'.
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total/count
    return add
avg = averager()
# Prova de que 'add' é uma 'closure' segue abaixo.
avg.__closure__
avg(5)
avg(10)

# É possível simplificar e tornar o código mais eficiente a partir do uso de 
# closures. 

def averager():
    total = 0
    count = 0
    def add(number):
        # É preciso tornar as variáveis 'total' e 'count' em variáveis não locais 
        # para que a "coisa" funcione.
        nonlocal total
        nonlocal count
        total = total+number
        count+=1
        return total/count
    return add

avg_10 = averager()
avg_10(50)
avg_10(100)