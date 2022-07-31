'''
This module contains basic configurations related to the project developed
in section 06.

Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base
from core.secret_gen import TOKEN

from core.db_sensitive_information import *

class Settings(BaseSettings):
    '''
    Class related to the general configuration of the application.
    '''
    API_V1_STR: str = '/api/v1' # base endpoint
    DB_URL: str = f'postgresql+asyncpg://{user_}:{password_}@{server_}'+ \
                  f':{port_}/{db_name}' # db configuration
    DBBaseModel = declarative_base() # this help the development of the SQLAlchemy models
    JWT_SECRET:str = TOKEN # token pattern
    ALGORITHM:str = 'HS256' # 
    ACCESS_TOKEN_EXPIRE_MINUTES:int = 60*24*7 # 1 week

    class Config:
        case_sensitive = True # upper and lower case letter are important for the Settings class.

settings_:Settings = Settings()
