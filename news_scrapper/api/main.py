from fastapi import FastAPI
import search_router 

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app.include_router(search_router.mongo_router, prefix="/search", tags=["Config"])
