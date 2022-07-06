# Validators.
'''
Arquivo de código do pacote 'validators'.
'''
# Os módulos abaixo estão sendo importados aqui, porque isso permite que, ao se
# importar o pacote 'validators', no módulo 'main', não se precise importar cada 
# módulo individualmente.
# Ao se se fazer as importações dessa forma, está a se trazer para o namespace de
# 'validators' todas as funções presentes em cada um desses módulos. 
print("Executando o pacote 'validators'.")
from .boolean import *
from  .date import *
from .json import *

# Para verificar o que está no 'namespace' do pacote 'validators'.
print(f'validators.__dict__ = {globals()}')
