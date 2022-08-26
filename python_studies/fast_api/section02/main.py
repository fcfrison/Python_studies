from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def root():
    return {"msg": "FastApi it's working fast..."}