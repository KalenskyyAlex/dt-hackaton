from fastapi import APIRouter

dataset_router = APIRouter()

@dataset_router.get("/get/{key}")
def get_by_key():
    return {
        "message": "test"
    }

@dataset_router.get("/list")
def list_by_query(query: str = None):
    return {
        "message": "test"
    }

@dataset_router.get("/")
def test():
    return {
        "message": "ok"
    }