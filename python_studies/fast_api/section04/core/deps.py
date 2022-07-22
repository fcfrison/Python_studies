'''
This module is for the dependecies of the API.
'''
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

from database import Session

async def get_session()->Generator:
    '''
    Coroutine that returns a session.
    '''
    session : AsyncSession = Session() # pointing to a new session (session is a generator)
    try:
        yield session # starting the generator
    finally:
        await session.close()

    