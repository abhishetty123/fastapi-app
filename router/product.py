from fastapi import APIRouter, Depends
from shemas.product import ProductSchema, ProductUpdateSchema
from sqlalchemy.orm import Session
from core.database import get_db
from typing import Annotated
from services.product import create_product_service, get_product_by_id_service,get_product_by_category_service,update_product_service,get_all_product_service,get_all_category_service,delete_product_service

router = APIRouter(
    prefix="/product",
    tags=["product"]
)
db_dependancy =  Annotated[Session, Depends(get_db)]
@router.post("/create")
def create_product(product : ProductSchema, db : db_dependancy):
    return create_product_service(product, db)

@router.get("/id/{product_id}")
def get_product_by_id(product_id:int, db:db_dependancy):
    return get_product_by_id_service(product_id, db)

@router.get("/category/{product_category}")
def get_product_by_category(product_category:str, db:db_dependancy):
    return get_product_by_category_service(product_category, db)

# @router.put("/update/{product_id}")
# def update_product(product_id : int ,product : ProductSchema, db:db_dependancy):
#     return update_product_by_id(product_id, product, db)

@router.patch("/update/{product_id}")
def update_product_partial(product_id : int ,product : ProductUpdateSchema, db:db_dependancy):
    return update_product_service(product_id, product, db)

@router.get("/all")
def get_all_product(db:db_dependancy):
    return get_all_product_service(db)

@router.get("/all_catagory")
def get_all_catagory (db:db_dependancy):
    return get_all_category_service(db)

@router.delete("/id/{product_id}")
def delete_product(id : int, db: db_dependancy):
    return delete_product_service(id,db)