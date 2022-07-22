

from fastapi import APIRouter

router = APIRouter() # instead of creating an object from the class FastAPI 
                     # it's better to create different routes, via APIRouter.

@router.get('/api/v1/users')
async def get_users():
    return {'info':'Returns all users registered in the database.'}
