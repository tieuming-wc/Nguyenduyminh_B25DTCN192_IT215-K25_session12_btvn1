from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import Base, engine, get_db
from model import ProductModel
from service import ProductUpdate

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.put("/products/{product_id}")
def update_product(
    product_id: int, 
    product_update: ProductUpdate, 
    db: Session = Depends(get_db)
):
    product = db.query(ProductModel).filter(ProductModel.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = product_update.name
    product.price = product_update.price

    db.commit()
    db.refresh(product)

    return {
        "message": "Product updated successfully",
        "data": {"id": product.id, "name": product.name, "price": product.price}
    }
