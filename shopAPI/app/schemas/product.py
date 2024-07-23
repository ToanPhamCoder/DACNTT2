from pydantic import BaseModel

class ProductSchema(BaseModel):
    id: str
    name: str
    url: str
    img: str
    sup: int
