'''
This module contains auth configurations related to the project developed
in section 06.

Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''
from pytz import timezone
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from pydantic import EmailStr
from jose import jwt
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union

from models.user_model import UserModel
from core.configs import settings_
from core.security import check_password

oauth2_schema = OAuth2PasswordBearer( # OAuth2PasswordBearer allows the creation of an access endpoint
    tokenUrl=f'{settings_.API_V1_STR}/users/login'
)

async def authentication(email:EmailStr, password:str, 
                db:AsyncSession)->Union[UserModel,None]:
    '''
    This coroutine checks if the user and the password are valid.
    '''
    async with db as session:
        query = select(UserModel).filter(UserModel.email==email)
        result = await session.execute(query)
        user: UserModel = result.scalars().unique().one_or_none()
        if not user: # user not found in db.
            return None
        if not check_password(password=password,
                            hash_password=user.password): # password incorrect
            return None
        return user

def _token_generator(token_type:str, duration:timedelta, subject:str)->str:
    '''
    Internal function for generating a token for a specific user.
    We are using the industry standard RFC 7519 as reference.
    '''
    payload = {}
    sp_tz: datetime.tzinfo = timezone('America/Sao_Paulo')
    expiration_time = datetime.now(tz=sp_tz) + duration
    payload['type'] = token_type
    payload['exp'] = expiration_time
    payload['iat'] = datetime.now(tz=sp_tz) # token issued at..
    payload['sub'] = str(subject) # sub is something that identify the user
    return jwt.encode(claims=payload, 
                      key=settings_.JWT_SECRET,
                      algorithm=settings_.ALGORITHM) # encoding the payload

def access_token_generator(sub:str)->str:
    '''
    Function that generates an access token.
    '''
    return _token_generator(token_type= 'access_token', 
                            duration= timedelta(minutes=settings_.ACCESS_TOKEN_EXPIRE_MINUTES), 
                            subject= sub)

