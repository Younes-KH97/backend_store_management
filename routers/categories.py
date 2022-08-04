from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy.orm import Session

from dependencies import get_db
import crud, schemas

router = APIRouter(
    prefix = "/categories",
    tags = ["categories"]
)

@router.get("/", response_model=list[schemas.Category])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    categories = crud.get_categories(db, skip=skip, limit=limit)
    return categories

@router.post('/', response_model=schemas.Category)
def add_category(category: schemas.CategoryBase, db: Session = Depends(get_db)):
    return crud.create_category(db, category)

@router.delete('/{category_id}')
async def delete_category_by_id(category_id: int = Path(...), db: Session = Depends(get_db)):
    category = crud.get_category_by_id(db, category_id)
    if category is None:
        raise HTTPException(status_code = 404, detail = "Category not found")
    return crud.delete_category(db, category)

@router.put('/{categorie_id}')
async def update_category(categorie_id: int = Path(...), category: schemas.CategoryBase = Body(...),
                          db: Session = Depends(get_db)):
    return crud.update_category(db, categorie_id, category)