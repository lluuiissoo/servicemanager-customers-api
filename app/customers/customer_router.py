from fastapi import APIRouter, Depends
from app.customers.customer_service import CustomerService
from app.customers.customer_models import NewCustomer, Customer
from app.core.auth.authorization import authorized, annonymous

router = APIRouter()

customer_service = CustomerService()

@router.get("", status_code=200, tags=["customers"])
async def get_customer():
    return {
        "id": "1",
        "full_name": "John Doe"
    }

@router.post("", status_code=201, response_model=Customer, tags=["customers"], dependencies=[Depends(annonymous)])
async def create_customer(new_customer: NewCustomer) -> Customer:
    return customer_service.create_customer(new_customer)

@router.put("/{id}", status_code=200, response_model=Customer, tags=["customers"], dependencies=[Depends(annonymous)])
async def update_customer(updated_customer: Customer) -> Customer:
    return customer_service.update_customer(updated_customer)

@router.delete("/{id}", status_code=204, tags=["customers"], dependencies=[Depends(annonymous)])
async def delete_customer(id: int) -> str:
    return customer_service.delete_customer(id)