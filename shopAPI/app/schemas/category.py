from pydantic import BaseModel

class CategorySchema(BaseModel):
    id: str
    name: str
    url: str
    img: str
    sup: int
