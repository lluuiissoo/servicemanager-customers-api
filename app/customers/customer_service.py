from app.customers.customer_models import NewCustomer, Customer

class CustomerService():
    """Handle customer logic"""

    def __init__(self) -> None:
        pass

    def create_customer(self, customer: NewCustomer) -> Customer:
        return Customer(
            Id=1,
            Name=customer.Name,
            Phone=customer.Phone
        )
    
    def update_customer(self, customer: Customer) -> Customer:
        return Customer(
            Id=customer.Id,
            Name=customer.Name,
            Phone=customer.Phone
        )
    
    def delete_customer(self, customer_id: int) -> str:
        return "Ok"

        
