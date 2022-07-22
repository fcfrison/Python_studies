'''
This module contains general configurations related to the project developed
in section 04.

Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

from  db_sensitive_information import *

class Settings(BaseSettings):
    '''
    Class related to the general configuration of the application.
    '''
    API_V1_STR: str = '/api/v1' # base endpoint
    DB_URL: str = f'postgresql+asyncpg://{user_}:{password_}@{server_}'+ \
                  f':{port_}/{server_name_}' # db configuration
    DBBaseModel = declarative_base() # this help the development of the models

    class Config:
        case_sensitive = True

settings_ = Settings()
