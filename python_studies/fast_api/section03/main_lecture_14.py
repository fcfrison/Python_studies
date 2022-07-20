'''
In the code below, follows the basics of the HTTP method 'POST' in Fast API.


Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''

from fastapi import FastAPI, HTTPException
from typing import Dict


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


if __name__=="__main__":
    import uvicorn
    uvicorn.run("main_lecture_12:app", host="localhost", # uvicorn is a server for assynchronous processing
                port=8000, log_level="info", reload=True)