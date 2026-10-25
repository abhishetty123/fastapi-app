from sqlalchemy.orm import Session
from models.product import Product as ProductModel
from shemas.procuct import Product

def create_product_service(product:ProductModel, db: Session):
    newProduct = ProductModel(name=product.name, price=product.price, category=product.category)
    db.add(newProduct)
    db.commit()
    db.refresh(newProduct)
    return(newProduct)

def get_product_by_id_service(product_id:int, db:Session):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()
    return product

def get_product_by_category_service(product_category:str, db:Session):
    product = db.query(ProductModel).filter(ProductModel.category == product_category).all()
    return product