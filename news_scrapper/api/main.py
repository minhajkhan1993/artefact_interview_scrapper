from fastapi import FastAPI
from api import search_router

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(search_router.mongo_router, prefix="/search", tags=["Mongo Search"])
