from sqlalchemy.orm import Session
from models.product import Product as ProductModel
from shemas.product import ProductSchema, ProductUpdateSchema
from fastapi import HTTPException
def create_product_service(product:ProductSchema, db: Session):
    newProduct = ProductModel(name=product.name, price=product.price, category=product.category)
    db.add(newProduct)
    db.commit()
    db.refresh(newProduct)
    return(newProduct)

def get_product_by_id_service(product_id:int, db:Session):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def get_product_by_category_service(product_category:str, db:Session):
    product = db.query(ProductModel).filter(ProductModel.category == product_category).all()
    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

def get_all_product_service(db:Session):
    product = db.query(ProductModel).all()
    return (product)

def get_all_category_service(db:Session):
    rows = db.query(ProductModel.category).distinct().all()
    return ([row[0] for row in rows])

def update_product_service(product_id:int, product: ProductUpdateSchema, db: Session):
    existing_product = get_product_by_id_service(product_id, db)
    if existing_product is None:
        raise HTTPException (status_code = 404, detail ="Product Not Found",)
    if product.name is not None:
        existing_product.name = product.name
    if product.price is not None:
        existing_product.price = product.price
    if product.category is not None:
        existing_product.category = product.category

    db.commit()
    db.refresh(existing_product)
    return(existing_product)

def delete_product_service(product_id:int, db:Session):
    product = get_product_by_id_service(product_id, db)
    if product is None:
        raise HTTPException(status_code=404, detail = "product not found")
    db.delete(product)
    db.commit()

    return{"product deleted successfully"}
