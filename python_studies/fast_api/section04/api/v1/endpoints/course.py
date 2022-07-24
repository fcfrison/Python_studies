from typing import List
from fastapi import (APIRouter, Depends, 
                    HTTPException, Response)
from fastapi import status

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.course_model import CourseModel
from schemas.course_schema import CourseSchema
from core.deps import get_session

router = APIRouter() 

#POST course
@router.post('/',status_code=status.HTTP_201_CREATED, 
                response_model=CourseSchema) # response_model determines the template of the response.
async def post_course(course:CourseSchema, # 'course' is json object that is transformed in a CourseSchema object (by Pydantic)
                      db:AsyncSession = Depends(get_session)): # it's necessary to connect to the db
    new_course = CourseModel(title=course.title, # creating a new row
                            lectures=course.lectures,
                            total_hours=course.total_hours)
    db.add(new_course)
    await db.commit() # commiting the data
    return new_course

# GET courses
@router.get('/', response_model=List[CourseSchema]) #response_model refers to the object returned via API
async def get_courses(db :AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CourseModel) # select from 'courses'
        result = await session.execute(query) # execute the query
        courses: List[CourseModel] = result.scalars().all()
        return courses

# GET course
@router.get('/{course_id}', response_model=CourseSchema,
                      status_code=status.HTTP_200_OK)
async def get_course(course_id:int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CourseModel).filter(CourseModel.id_==course_id)
        result = await session.execute(query)
        course = result.scalar_one_or_none() # brings back one row or none
        if course:
            return course
        else:
            raise HTTPException(detail="Course not found.",
                                status_code=status.HTTP_404_NOT_FOUND)

# PUT course
@router.get('/{course_id}', response_model=CourseSchema,
                      status_code=status.HTTP_202_ACCEPTED)
async def put_course(course_id:int, course:CourseSchema, 
                    db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CourseModel).filter(CourseModel.id_==course_id)
        result = await session.execute(query)
        course_update = result.scalar_one_or_none() # brings back one row or none
        if course_update: # if the course was found, then update.
            course_update.title = course.title
            course_update.lectures = course.lectures
            course_update.total_hours = course.total_hours
            await session.commit()
            return course_update

        else:
            raise HTTPException(detail="Course not found.",
                                status_code=status.HTTP_404_NOT_FOUND)


# DELETE course
@router.get('/{course_id}', response_model=CourseSchema)
async def delete_course(course_id:int, db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CourseModel).filter(CourseModel.id_==course_id)
        result = await session.execute(query)
        course_delete = result.scalar_one_or_none() # brings back one row or none
        if course_delete: # if the course was found, then delete.
            await session.delete(course_delete)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        else:
            raise HTTPException(detail="Course not found.",
                                status_code=status.HTTP_404_NOT_FOUND)