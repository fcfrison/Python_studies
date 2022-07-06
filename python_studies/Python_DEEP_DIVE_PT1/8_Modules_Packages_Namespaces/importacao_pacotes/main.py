# Essa importação permite que sejam acessados diretamente todos os módulos 
# presentes em 'validators'.
import common_novo
import common_novo.validators as validators
#import common_novo.models.posts
#import common_novo.models.users
import common_novo.models

# O namespace de main.py é composto por:
print(globals().keys())

# O namespace do pacote 'validators' é composto por:
print(validators.__dict__.keys())
# É possível o acesso direto às funções, a partir do pacote 'validators', uma 
# vez que tais nomes constam no namespace de 'validators'.
validators.is_date('17/10/2021')

validators.is_boolean(True)

# Já o namespace do pacote 'common_novo' é composto por.  
print(common_novo.__dict__.keys())

# O namespace do pacote 'models' é composto por:
print(common_novo.models.__dict__.keys())

# O namespace do pacote 'posts' é composto por:
print(common_novo.models.posts.__dict__.keys())


