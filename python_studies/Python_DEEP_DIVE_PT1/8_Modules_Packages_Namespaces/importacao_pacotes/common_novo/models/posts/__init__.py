# posts
print('\nExecutando posts.__init__.py.\n')
from .post import *
from .posts import *

# Definindo quais as funções que serão importadas para o namespace do pacote 
# 'posts'. OBS.: essa importação é possível, pois tanto o módulo 'post', quanto
# o módulo 'posts' residem no namespace do pacote 'posts'.
__all__ = post.__all__ + posts.__all__
print(f'O namespace de "posts" é composto por: {globals().keys()}')
