from pydantic import BaseModel

class OrderSchema(BaseModel):
    orderID: str
    userId: str
    items: list
