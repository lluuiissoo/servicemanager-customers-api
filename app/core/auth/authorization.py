from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

security = HTTPBearer()

async def annonymous():
    return True

async def authorized(credentials: HTTPAuthorizationCredentials = Depends(security)):
    return True