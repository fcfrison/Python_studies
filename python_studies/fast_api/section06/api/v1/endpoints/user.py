from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError
from sqlalchemy.future import select

from typing import List, Optional

from core.auth import access_token_generator, authentication
from core.deps import get_current_user, get_session
from core.security import hash_generator
from models.user_model import UserModel
from schemas.user_schema import *

router = APIRouter()

# GET logged user
@router.get('/logged', response_model=UserSchemaBase)
def get_logged(logged_user: UserModel = Depends(get_current_user)):
    return logged_user

# POST /sign up
@router.post('/signup', status_code=status.HTTP_201_CREATED, 
            response_model=UserSchemaBase)
async def post_user(user:UserSchemaCreate,
                    db:AsyncSession=Depends(get_session)):
    new_user: UserModel = UserModel(
        name = user.name,
        last_name = user.last_name,
        email = user.email,  
        password = hash_generator(user.password),
        is_admin = user.is_admin
    )
    async with db as session:
        try:
            session.add(new_user)
            await session.commit() # here, the new data is inserted in the db
            return new_user
        except IntegrityError:
            raise HTTPException(detail="User already exists :-(.",
                                status_code=status.HTTP_409_CONFLICT)

# GET users
@router.get('/',response_model=List[UserSchemaBase])
async def get_users(db: AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(UserModel) # select all data from users table.
        result = await session.execute(query) # executing the query
        users: List[UserSchemaBase] = result.scalars().unique().all()
        return users
    
# GET user
@router.get('/{id_user}', response_model=UserSchemaPapers,
            status_code = status.HTTP_200_OK)
async def get_user(id_user:int,
                    db: AsyncSession=Depends(get_session)
                    ):
    async with db as session:
        query = select(UserModel).filter(UserModel.id==id_user)
        result = await session.execute(query)
        user = result.scalars().unique().one_or_none() # brings back one row or none
        if user:
            return user
        else:
            raise HTTPException(detail="User not found :-(.",
                                status_code=status.HTTP_404_NOT_FOUND)

# UPDATE user
@router.put('/{user_id}', response_model=UserSchemaPapers,
            status_code = status.HTTP_202_ACCEPTED)
async def put_user(user_id:int,
                    user_passed: UserSchemaUpdate,
                    db: AsyncSession=Depends(get_session),
                    user_model:UserModel=Depends(get_current_user)
                    ):
    async with db as session:
        query = select(UserModel).filter(UserModel.id==user_id)
        result = await session.execute(query)
        user = result.scalars().unique().one_or_none() # brings back one row or none
        if user:
            if user.id!=user_model.id:
                raise HTTPException(detail="User cannot update.",
                                status_code=status.HTTP_401_UNAUTHORIZED)
            if user_passed.name:
                user.name = user_passed.name
            if user_passed.last_name:
                user.last_name = user_passed.last_name
            if user_passed.email:
                user.email = user_passed.email
            if user_passed.password:
                user.password = user_passed.password
            if user_passed.is_admin:
                user.is_admin = hash_generator(user_passed.is_admin)
            await session.commit()

            return user
        else:
            raise HTTPException(detail="User not found.",
                                status_code=status.HTTP_404_NOT_FOUND)
                            
# DELETE user
@router.delete('/{id_user}', status_code = status.HTTP_204_NO_CONTENT)
async def delete_user(id_user:int,
                    db: AsyncSession=Depends(get_session)
                    ):
    async with db as session:
        query = select(UserModel).filter(UserModel.id==id_user)
        result = await session.execute(query)
        user = result.scalars().unique().one_or_none() # brings back one row or none
        if user:
            await session.delete(user)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail="User not found.",
                                status_code=status.HTTP_404_NOT_FOUND)

# POST login user 
@router.post('/login')
async def login(form_data:OAuth2PasswordRequestForm=Depends(),
                db: AsyncSession = Depends(get_session)): # form_data is a default form for data and password
        user = await authentication(email=form_data.username,
                                    password=form_data.password,
                                    db=db)
        if not user:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Wrong user or password.')
        return JSONResponse(content={
            "access_token":access_token_generator(sub=user.id),
            "token_type":"bearer"
            },
            status_code=status.HTTP_200_OK)
