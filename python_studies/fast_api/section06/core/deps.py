from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from pydantic import BaseModel
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from typing import Generator, Optional

from core.database import Session
from core.auth import oauth2_schema
from core.configs import settings_
from models.user_model import UserModel

class TokenData(BaseModel):
    username:Optional[str] = None

async def get_session()->Generator:
    '''
    This coroutine opens a database session, given the admin credentials.
    '''
    session: AsyncSession = Session()
    try:
        yield session # starts the session and returns it
    finally:
        await session.close() # close the connection

async def get_current_user(
        db: Session = Depends(get_session),
        token: str = Depends(oauth2_schema))->UserModel:
    '''
    This coroutine get a token and returns the user related to the
    passed token.
    '''
    credential_exception = HTTPException( # creating an HTTP exception
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = 'The authentication has failed.',
        headers={'WWW-Authenticate':'Bearer'}
    )
    try:
        payload = jwt.decode( # decoding the payload informed by the user
            token = token,
            key = settings_.JWT_SECRET,
            algorithms=[settings_.ALGORITHM],
            options={'verify_aud':False}
        )
        username:str = payload.get('sub') # getting the username reference
        if (username is None):
            raise credential_exception
        
        token_data = TokenData(username=username) # instantiating an object by TokenData
    except JWTError:
        raise credential_exception
    
    # checking in the db if the passed username is valid
    async with db as session:
        query = select(UserModel).filter(UserModel.id==int(token_data.username))
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()
        if user is None:
            raise credential_exception
        return user
        
