from fastapi import APIRouter

router = APIRouter()

@router.get("", status_code=200)
async def liveness():
    return {
        "message": "I am alive"
    }