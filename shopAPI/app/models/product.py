from pydantic import BaseModel

class Product(BaseModel):
    id: str
    name: str
    url: str
    img: str
    sup: int
