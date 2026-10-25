from fastapi import APIRouter, Depends
from shemas.procuct import Product
from sqlalchemy.orm import Session
from core.database import get_db
from typing import Annotated
from services.product import create_product_service, get_product_by_id_service,get_product_by_category_service

router = APIRouter(
    prefix="/product",
    tags=["product"]
)
db_dependancy =  Annotated[Session, Depends(get_db)]
@router.post("/create")
def create_product(product : Product, db : db_dependancy):
    return create_product_service(product, db)

@router.get("/product_id")
def get_product_by_id(product_id:int, db:db_dependancy):
    return get_product_by_id_service(product_id, db)

@router.get("/product_category")
def get_product_by_category(product_category:str, db:db_dependancy):
    return get_product_by_category_service(product_category, db)