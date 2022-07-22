'''
This module contains the Python objects related to the PostgreSQL
database.
'''

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession

from configs import settings_

engine: AsyncEngine = create_async_engine(settings_) # creating an asynchronous engine
Session: AsyncSession = sessionmaker( # instantiating a session
    autocommit=False, # commits are manual
    autoflush=False, 
    expire_on_commit=False, # session stays open after a commit
    bind=engine
)
