# users
print('\n Executando users.__init__.py.\n')
from .user import *
__all__ = user.__all__
print(f'O namespace do pacote "users" é composto por {globals().keys()}\n')