from fastapi import FastAPI
from router.user import router as user_router
from router.product import router as product_router
# from router.cart import cart as cart_router
from core.database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()


app.include_router(user_router)
app.include_router(product_router)
# app.include_router(cart_router)

@app.get("/")
async def root():
    return {"message": "message from root"}






