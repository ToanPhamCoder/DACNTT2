from fastapi import APIRouter, File, UploadFile
from app.services.category_service import get_frequent_categories, add_categories, get_all_categories

router = APIRouter()

@router.get("")
async def category():
    return await get_frequent_categories()

@router.post("/add")
async def addOrders(file: UploadFile = File(...)):
    return await add_categories(file)

@router.get("/all")
async def getCategorys(size: int = 10, page : int = 0):
    return await get_all_categories(page,size)