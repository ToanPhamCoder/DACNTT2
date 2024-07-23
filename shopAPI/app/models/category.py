from pydantic import BaseModel

class Category(BaseModel):
    id: str
    name: str
    url: str
    img: str
    sup: int
