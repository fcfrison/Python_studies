'''
Instead of executing the file via terminal, it's possible 
to do so through the __name__ variable.
'''

from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get('/')
async def root():
    return {"msg":"FastApi it's working..."}

if __name__=="__main__":
    uvicorn.run("main:app", host="localhost", # uvicorn is a server for assynchronous processing
                port=8800, log_level="info", reload=True)