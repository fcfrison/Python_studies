# models

# As importações abaixo farão com que tudo o que está no namespace do pacote 
# 'posts' e o que está no pacote 'users' sejam trazido para o namespace de 
# 'models'. 
print('\nExecutando models.__init__.py.\n')
from .posts import *
from .users import *

# Isso faz com que apenas o que está em posts.__init__.__all__ e 
# users.__init__.__all__ seja importado.
__all__ = posts.__all__ + users.__all__
print(f'O namespace de {__name__} é composto por: {globals().keys()}')

