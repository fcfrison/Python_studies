from fastapi import APIRouter
from api.v1.endpoints import course

api_router = APIRouter()
api_router.include_router(course.router,prefix='/courses',tags=['courses']) #include the routes created.