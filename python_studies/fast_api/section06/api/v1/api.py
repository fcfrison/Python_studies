from fastapi import APIRouter

from api.v1.endpoints import paper, user

api_router = APIRouter()

api_router.include_router(paper.router, prefix='/papers', tags=['papers'])
api_router.include_router(user.router, prefix='/users', tags=['users'])