from fastapi import APIRouter,File, UploadFile
from app.services.order_service import add_Order, get_Order

router = APIRouter()

@router.post("/add")
async def addOrders(file: UploadFile = File(...)):
    return await add_Order(file)

@router.get("/all")
async def getOrders(size: int = 10, page : int = 0):
    return await get_Order(page,size)