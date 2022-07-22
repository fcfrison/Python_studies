'''
The main file just agregates the routes created in the other 
modules.

Code related to the course "FastAPI - APIs Modernas e Assíncronas com Python". 
Available at https://www.udemy.com/course/fastapi-apis-modernas-e-assincronas-com-python/
'''
from fastapi import FastAPI
from routes import course_router, user_router

app = FastAPI()

# incluiding routes
app.include_router(course_router.router,tags=['courses'])
app.include_router(user_router.router,tags=['users'])

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", 
                port=8000, log_level="info", reload=True)
