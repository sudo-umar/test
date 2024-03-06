from fastapi import FastAPI

app = FastAPI()


@app.get('/routes')
async def get_routes():
    return {"message": "hello world"}
