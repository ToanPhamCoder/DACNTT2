from fastapi import APIRouter, File, UploadFile
from app.services.product_service import get_frequent_products, search_product, get_related_items, add_products, get_all_products

router = APIRouter()

@router.get("")
async def products():
    return await get_frequent_products()

@router.get("/search")
async def product(name: str = None):
    return await search_product(name)

@router.get("/related")
async def related_items(url: str = None):
    return await get_related_items(url)

@router.post("/add")
async def addProducts(file: UploadFile = File(...)):
    return await add_products(file)

@router.get("/all")
async def getProducts(size: int = 10, page : int = 0):
    return await get_all_products(page,size)