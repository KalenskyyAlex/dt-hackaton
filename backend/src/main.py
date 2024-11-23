from fastapi import FastAPI
from api.dataset import dataset_router

app = FastAPI()

# Include example routes
app.include_router(dataset_router, prefix="/dataset")

@app.get("/")
async def root():
    return {"message": "Welcome to FastAPI!"}
