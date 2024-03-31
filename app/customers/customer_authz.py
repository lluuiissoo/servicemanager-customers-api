from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from config import settings
import logging
from typing import List
from pydantic import BaseModel
from jose import jwt
from jose.exceptions import JOSEError

async def can_create(request: Request) -> bool:
    resource = "customers"
    role = "create"
    authz_service = AuthZService(request)

security = HTTPBearer()

class AuthZService():
    def __init__(self) -> None:
        self._is_enabled = settings.AUTHZ_ENABLED
        if not self._is_enabled:
            logging.warning("Authorization is disabled in settings!!!")
    
    async def is_authorized(self, request: Request, role: str) -> bool:
        if not self._is_enabled:
            logging.warning("Authorization is disabled in settings!!!")
            return True
        
        # Extract JWT from request
        credentials: HTTPAuthorizationCredentials = await security(request)
        jwt_token = credentials.credentials

        jwt_service = JWTService()
        token: JWTModel = jwt_service.decode_jwt(jwt_token)

        if not self._has_role(role, token.claims):
            self._raise_403(role, token.claims)
        
        return True
        
    def _has_role(self, role_to_check: str, token_claims: List[str]) -> bool:
        return role_to_check in token_claims


class JWTModel(BaseModel):
    claims: List[str]

class JWTService():
    def __init__(self, request: Request) -> None:
        self._request = request

    def decode_jwt(jwt_token: str) -> JWTModel:
        try:
            payload = jwt.decode(
                jwt_token,
                key="secret",
                options={
                    "verify_signature": False,
                    "verify_aud": False, # No need to check for this since auth is enabled and Azure will do it ootb
                    "verify_iss": False,
                }
            )

            # Deserialize token json into object
            auth_token = JWTModel(**payload)

        except JOSEError as e: # Catch any exception, including expired tokens
            raise HTTPException(status_code=401, detail=str(e))


        


