from fastapi import FastAPI

from api.v1.api import api_router
from core.configs import settings_

app = FastAPI(title='FAST API crashcourse')
app.include_router(api_router,prefix=settings_.API_V1_STR)

if __name__=="__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", # uvicorn is a server for assynchronous processing
                port=8000, log_level="info", reload=True)