'''
Sometimes, it's possible that the execution of a function depends on 
the previous execution of another function.

For example, to select data from a database, it's necessary to connect to
the database.

Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''


from time import sleep
from fastapi import Depends, FastAPI, HTTPException, Header, Path, Query
from fastapi import status
from fastapi.responses import JSONResponse, Response
from typing import Any, Dict, Optional
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

def db_connect():
    '''
    Function that emulates the dinamics of a connection to the 
    database.
    '''
    try:
        print("Open a connection to the database...")
        sleep(1)
    finally:
        print("Closing the connection to the database...")
        sleep(1)

# Dependencies here !!!!!!
@app.get("/courses")
async def get_courses(db:Any = Depends(db_connect))->dict:
    '''
    Coroutine that returns a dictionary with the given courses
    in a period of time.

    The execution of this coroutine depends on the previous execution
    of the function 'db_connect'.
    '''
    return courses

@app.get("/courses/{id}") 
async def get_course(id:int = Path(default=None, title='course id',
                                    description='The id is a positive number',
                                    gt=0))->dict:   # here is an case use of path parameters.
                                                    # In this example, the value must be greater than 0.
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
async def post_course(course:Course,db:Any = Depends(db_connect)): 
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
async def put_course(course_id:int, course:Course,db:Any = Depends(db_connect)):
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
async def delete_course(course_id:int,db:Any = Depends(db_connect))->dict:
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
# Header parameters here!!!!!!!
@app.get('/calculator')
async def calculate(a:int = Query(default=0, gt=-1), # all arguments must be positive.
                    b:int = Query(default=0, gt=-1), 
                    c:int = Query(default=0, gt=-1),
                    x_header:str = Header(default="The header is empty"))->dict:
    '''
    Coroutine that sums three values passed as arguments.
    The values must be passed as query parameters.

    Example: 
    localhost:8800/calculator?a=1&b=2&c=3

    Also, considering that a header parameter was defined, 
    it's possible to pass information via header. 
    '''
    sum_ = a+b+c
    print(f'header value = {x_header}')
    return {'result':sum_}

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main_lecture_20:app", host="localhost", # uvicorn is a server for assynchronous processing
                port=8800, log_level="info", reload=True)