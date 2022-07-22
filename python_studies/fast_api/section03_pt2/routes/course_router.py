'''
It's important to structure the API project in a way that makes its 
understanding easier. Instead of creating just one file with all
endpoints, it's a better approach to create multiple modules with
different routes.

Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''

from fastapi import APIRouter

router = APIRouter() # instead of creating an object from the class FastAPI 
                     # it's better to create different routes, via APIRouter.

@router.get('/api/v1/courses')
async def get_courses():
    return {'info':'Returns all courses registered in the database.'}