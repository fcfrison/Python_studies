'''
In the code below, follows the basics of the HTTP method 'DELETE' in Fast API.


Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''

from fastapi import FastAPI, HTTPException
from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Dict
from models import Course


app = FastAPI()

courses : Dict[int,dict] = { # the variable 'courses' is suposed to functions as a mini database
    1: {
        'title' : 'Crashcourse Python',
        'lectures' : 30,
        'duration' : 10
    }, 
    2: {
        'title' : 'Crashcourse Java',
        'lectures' : 110,
        'duration' : 50
    },

}

@app.get("/courses")
async def get_courses()->dict:
    '''
    Coroutine that returns a dictionary with the given courses
    in a period of time.
    '''
    return courses

@app.get("/courses/{id}") 
async def get_course(id:int)->dict: # it's very import to use type hints, 
                                    #because FastAPI uses pydantic by default
    '''
    Coroutine that returns a dictionary with the courses who matches 
    the given id.
    '''
    try:
        course = courses[id]
        course.update({"course_id" : id}) #update the dictionary
        return course
    except KeyError:
        raise HTTPException(status_code=404, detail="Course not found in the database.")

@app.post("/courses",status_code=status.HTTP_201_CREATED)
async def post_course(course:Course): 
    '''
    Coroutine that insert new data in the database.
    '''

    '''
    Given that fastAPI relies on Pydantic, it's not necessary
    to manually create an instance of the class Course. In other
    words, considering that a json file was sent to the API, 
    the convertion to a Course object is automatic.
    '''  
    next_id:int = len(courses) + 1
    del course.id
    courses[next_id] = course
    return course

@app.put('/courses/{course_id}', status_code=status.HTTP_202_ACCEPTED)
async def put_course(course_id:int, course:Course):
    '''
    Coroutine that update existing data in the database.
    '''
    if (course_id in courses):
        del course.id
        courses[course_id] = course
        return course
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Course not found in the database.")

@app.delete('/courses/{course_id}', status_code=status.HTTP_200_OK)
async def delete_course(course_id:int)->dict:
    '''
    Coroutine that deletes existing data in the database.
    '''
    if (course_id in courses):
        courses.pop(course_id)
        #return JSONResponse(content=None,
        #    status_code=status.HTTP_204_NO_CONTENT)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Course not found in the database.")

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main_lecture_16:app", host="localhost", # uvicorn is a server for assynchronous processing
                port=8800, log_level="info", reload=True)