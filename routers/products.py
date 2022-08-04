from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy.orm import Session
import crud, schemas
from dependencies import get_db

router = APIRouter(
    prefix = "/products",
    tags = ["products"]
)


@router.get("/", response_model=list[schemas.Product])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud.get_products(db, skip=skip, limit=limit)
    return products

@router.post('/{category_id}', response_model=schemas.Product)
def add_product(product: schemas.ProductBase, category_id: int = Path(...), db: Session = Depends(get_db)):
    return crud.create_product(db, product, category_id)


@router.delete('/{product_id}')
def delete_product_by_id(product_id: int = Path(...), db: Session = Depends(get_db)):
    product = crud.get_product_by_id(db, product_id)
    if product is None:
        raise HTTPException(status_code = 404, detail = "Product not found")
    return crud.delete_product(db, product)

@router.put('/{product_id}')
def update_product(product_id: int = Path(...), product: schemas.ProductBase = Body(...),
                         db: Session = Depends(get_db)):
    return crud.update_product(db, product_id, product)