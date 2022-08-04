from fastapi import APIRouter, Body, Depends, HTTPException, Path
from sqlalchemy.orm import Session
import crud, schemas
from dependencies import get_db

router = APIRouter(
    prefix = "/roles",
    tags = ["roles"]
)


@router.get('/', response_model = list[schemas.Role])
async def get_all_roles(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return crud.get_all_roles(db, skip, limit)

@router.post('/', response_model = schemas.Role)
async def create_role(role: schemas.RoleBase, db: Session = Depends(get_db)):
    return crud.create_role(db, role)

@router.delete('/{role_id}')
async def delete_role_by_id(role_id: int = Path(...), db: Session = Depends(get_db)):
    role_db = crud.get_role_by_id(db, role_id)
    return crud.delete_role(db, role_db)

@router.put('/{role_id}')
def update_role(role_id: int = Path(...), role: schemas.RoleBase = Body(...), db: Session = Depends(get_db)):
    return crud.update_role(db, role_id, role)
