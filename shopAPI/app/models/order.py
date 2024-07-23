from pydantic import BaseModel

class Order(BaseModel):
    orderID: str
    userId: str
    items: list
