from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy.orm import Session
import crud, schemas
from dependencies import get_db

router = APIRouter(
    prefix = "/product_types",
    tags = ["product_types"]
)



@router.get("/", response_model=list[schemas.ProductType])
def read_product_types(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_product_types(db, skip=skip, limit=limit)


@router.post('/{product_id}', response_model = schemas.ProductType)
def add_category_to_product(product_type: schemas.ProductTypeBase, product_id: int = Path(...), db: Session = Depends(get_db)):
    return crud.create_product_type(db, product_type, product_id)

@router.delete('/{product_id}', response_model = schemas.ProductType)
def delete_product_by_id(product_id: int = Path(...), db: Session = Depends(get_db)):
    product = crud.get_product_type_by_id(db, product_id)
    return crud.delete_product_by_id(db, product)

@router.put('/{product_type_id}')
async def update_product_type_id(product_type_id: int = Path(...), product_type: schemas.ProductType = Body(...),
                                 db: Session = Depends(get_db)):
    return crud.update_product_type(db, product_type_id, product_type)
