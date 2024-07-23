from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.utils.database import get_database
from app.routes import category, order, product

app = FastAPI(
    title="Ứng dụng để xuất Bachhoaxanh",
    summary="Một ứng dụng đơn giản giúp cho việc đi chợ của con người trở nên đơn giản",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

db = get_database()

app.include_router(category.router, prefix="/category", tags=["Category"])
app.include_router(product.router, prefix="/products", tags=["Product"])
app.include_router(order.router, prefix="/order",tags=["Order"])

@app.get("/home/")
async def home():
    return "welcome"

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
