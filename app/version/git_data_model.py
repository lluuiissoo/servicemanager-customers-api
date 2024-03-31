from pydantic import BaseModel

class GitData(BaseModel):
    commit: str
    branch: str
