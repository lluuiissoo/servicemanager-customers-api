from pydantic import BaseModel
# from typing import Optional

class NewCustomer(BaseModel):
    Name: str
    Phone: str

class DeleteCustomer(BaseModel):
    Id: int

class Customer(BaseModel):
    Id: int
    Name: str
    Phone: str
