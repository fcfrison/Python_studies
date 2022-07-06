'''
'timeit' é um módulo utilizado para verificar o tempo de execução de uma 
função.
'''
from timeit import timeit
# Vamos imaginar que se deseje mensurar a velocidade de dois métodos distintos
# de importação. 
from math import sqrt
import math
# Primeira forma de se utilizar timeit para testar algo. A configuração está 
# dessa forma, uma vez que timeit possui escopo próprio para as variáveis.
timeit(stmt='sqrt(1005)',setup='from math import sqrt', number=1_000_000)
timeit(stmt='math.sqrt(1005)',setup='import math', number=1_000_000)

# A segunda forma é fazendo com que 'timeit' procure pelos nomes no escopo global 
# do presente módulo. 
timeit(stmt='sqrt(1005)',globals=globals(), number=1_000_000)
timeit(stmt='math.sqrt(1005)',globals=globals(), number=1_000_000)

# A depender da situação, é possível que tenha que se misturarem ambos os métodos.
import random
l = random.choices(list('python'), k=500)
# No caso abaixo, está se trazendo para o escopo de 'timeit' o pacote 'random'. 
# Ao mesmo tempo, a variável 'l' está no escopo global do módulo. Logo, é 
# necessário buscá-la neste escopo. 
timeit(stmt='random.choice(l)',setup='import random',globals=globals(),number=1_000_000)

