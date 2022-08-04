from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy.orm import Session
import crud, schemas
from dependencies import get_db

router = APIRouter(
    prefix = "/users",
    tags = ["users"]
)


@router.get('/', response_model = list[schemas.User])
async def get_all_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_users(db, skip, limit)

@router.post('/', response_model = schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)

@router.post('/role/{user_id}/{role_id}', response_model = schemas.User)
async def add_role_to_user(user_id: int = Path(...), role_id: int = Path(), db: Session = Depends(get_db)):
    user_db = crud.get_user_by_id(db, user_id)
    role_db = crud.get_role_by_id(db, role_id)
    return crud.add_role_to_user(db, user_db, role_db)

@router.delete('/{user_id}')
async def delete_user(user_id: int = Path(...), db: Session = Depends(get_db)):
    user_db = crud.get_user_by_id(db, user_id)
    return crud.delete_user(db, user_db)

@router.delete('/roles/{user_id}/{role_id}', response_model = schemas.User)
async def delete_role_from_user(user_id: int = Path(...), role_id: int = Path(...), db: Session = Depends(get_db)):
    role_db = crud.get_role_by_id(db, role_id)
    user_db = crud.get_user_by_id(db, user_id)

    return crud.delete_role_from_user(db, user_db, role_db)

@router.post('/wishes/{user_id}/{product_id}', response_model = schemas.User)
async def add_wished_product(user_id: int = Path(...), product_id: int = Path(...), db: Session = Depends(get_db)):
    product_db = crud.get_product_by_id(db, product_id)
    user_db = crud.get_user_by_id(db, user_id)

    return crud.add_product_wished(db, user_db, product_db)

@router.delete('/wishes/{user_id}/{product_id}', response_model = schemas.User)
async def delete_wished_product(user_id: int = Path(...), product_id: int = Path(...), db: Session = Depends(get_db)):
    product_db = crud.get_product_by_id(db, product_id)
    user_db = crud.get_user_by_id(db, user_id)

    return crud.delete_wished_product(db, user_db, product_db)

@router.post('/orders/{user_id}', response_model = list[schemas.Product_Order_In])
async def create_new_order(user_id: int = Path(...), products_order_in: list[schemas.Product_Order_In] = Body(...), db: Session = Depends(get_db)):
    user_db = crud.get_user_by_id(db, user_id)
    user_order = crud.create_order(db, user_db)
    return crud.create_products_order(db, user_order, products_order_in)

@router.delete('/orders/{order_id}')
async def delete_user_order_by_id(order_id: int = Path(...), db: Session = Depends(get_db)):
    order = crud.get_order_by_id(db, order_id)
    return crud.delete_order_from_user(db, order)

@router.put('/{user_id}')
async def update_user(user_id: int = Path(...), 
                      user_create: schemas.UserCreate = Body(...),
                      db: Session = Depends(get_db)):
    return crud.update_user(db, user_id, user_create)


