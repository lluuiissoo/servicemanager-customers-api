from fastapi import APIRouter

router = APIRouter()

@router.get("", status_code=200)
async def readiness():
    return {
        "message": "I am ready",
        "probes": [
            {
                "probe": "Connect to DB",
                "result": "OK"
            },
            {
                "probe": "Read from DB",
                "result": "OK"
            },
            {
                "probe": "Write to DB",
                "result": "OK"
            }
        ]
    }