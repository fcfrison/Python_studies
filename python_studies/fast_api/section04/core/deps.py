'''
This module is for the dependecies of the API.
'''
from typing import Generator
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import Session

async def get_session()->Generator:
    '''
    Coroutine that yields a session.
    '''
    session : AsyncSession = Session() # pointing to a new session (session is a generator)
    try:
        yield session # starting the generator and return its memory reference
    finally:
        await session.close()

    