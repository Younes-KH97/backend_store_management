from datetime import datetime
from msilib import schema
from fastapi import HTTPException
from sqlalchemy import delete, insert, null, select
from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder
import models, schemas


def get_category_by_id(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()


def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_category(db: Session, category: schemas.CategoryBase):
    db_category = models.Category(**category.dict())
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category: schemas.CategoryBase):
    db.delete(category)
    db.commit()
    return category

def update_category(db: Session, category_id: int, category: schemas.CategoryBase):
    stmt = select(models.Category).where(models.Category.id == category_id)
    category_db = db.scalars(stmt).one()

    category_db.name = category.name
    category_db.photo_url = category.photo_url

    db.commit()
    db.refresh(category_db)

    return {"detail": "category updated successfully"}




def get_products(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product_by_id(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductBase, category_id: int):
    db_product = models.Product(**product.dict(), category_id = category_id)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def delete_product(db: Session, product: schemas.ProductBase):
    db.delete(product)
    db.commit()
    return product

def update_product(db: Session, product_id: int, product: schemas.ProductBase):
    stmt = select(models.Product).where(models.Product.id == product_id)
    product_db = db.scalars(stmt).one()

    product_db.title = product.title
    product_db.description = product.description
    product_db.price = product.price
    product_db.time = product.time
    product_db.photo_url = product.photo_url

    db.commit()
    db.refresh(product_db)

    return {"detail": "product updated successfully"}


def get_product_types(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.ProductType).offset(skip).limit(limit).all()

def create_product_type(db: Session, product_type: schemas.ProductTypeBase, product_id):
    db_product_type = models.ProductType(**product_type.dict(), product_id = product_id)
    db.add(db_product_type)
    db.commit()
    db.refresh(db_product_type)
    return db_product_type

def get_product_type_by_id(db: Session, product_type_id: int):
    return db.query(models.ProductType).filter(models.ProductType.id == product_type_id).first()

def delete_product_by_id(db: Session, product_type: schemas.ProductType):
    db.delete(product_type)
    db.commit()
    return product_type

def update_product_type(db: Session, product_type_id: int, product_type: schemas.ProductType):
    stmt = select(models.ProductType).where(models.ProductType.id == product_type_id)
    product_type_db = db.scalars(stmt).one()

    product_type_db.name = product_type.name

    db.commit()
    db.refresh(product_type_db)

    return {"detail": "product_type updated successfully"}

def get_all_users(db: Session, skip, limit):
    return db.query(models.User).offset(skip).limit(limit).all()

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user: schemas.User):
    db.delete(user)
    db.commit()
    return {
        "message": f"user: {user.username} is deleted successfully"
    }

def update_user(db: Session, user_id: int, user_create: schemas.UserCreate):
    stmt = select(models.User).where(models.User.id == user_id)
    user = db.scalars(stmt).one()

    user.username = user_create.username
    user.password = user_create.password
    user.email = user_create.email

    db.commit()
    return {"detail": "User updated successfully"}



def add_role_to_user(db: Session, user: schemas.User, role: schemas.Role):
    user.roles.append(role)
    db.commit()
    return user

def delete_role_from_user(db: Session, user: schemas.User, role: schemas.Role):
    user.roles.remove(role)
    db.commit()
    return user

# def delete_product(db: Session, product: schemas.ProductBase):
#     db.delete(product)
#     db.commit()
#     return product

def get_all_roles(db: Session, skip, limit):
    return db.query(models.Role).offset(skip).limit(limit).all()

def get_role_by_id(db: Session, role_id: int):
    return db.query(models.Role).filter(models.Role.id == role_id).first()

def create_role(db: Session, role: schemas.RoleBase):
    db_role = models.Role(**role.dict())
    db.add(db_role)
    db.commit()
    db.refresh(db_role)
    return db_role


def delete_role(db: Session, role: schemas.Role):
    db.delete(role)
    db.commit()
    return {
        "message": f"role: {role.name} is deleted successfully"
    }

def update_role(db: Session, role_id: int, role: schemas.RoleBase):
    stmt = select(models.Role).where(models.Role.id == role_id)
    role_db = db.scalars(stmt).one()

    role_db.name = role.name

    db.commit()
    db.refresh(role_db)

    return {"detail": "Role updated successfully"}

def delete_order_from_user(db: Session, order: schemas.UserOrder):
    db.delete(order)
    db.commit()
    return {"details": "The order is deleted successfuly"}

def add_product_wished(db: Session, user: schemas.User, product: schemas.Product):
    user.wish_list.append(product)
    db.commit()
    return user

def delete_wished_product(db: Session, user: schemas.User, product: schemas.Product):
    user.wish_list.remove(product)
    db.commit()
    return user

###
def get_order_by_id(db: Session, order_id: int):
    return db.query(models.UserOrder).filter(models.UserOrder.id == order_id).first()

def create_order(db: Session, user: schemas.User):
    date_time = {"date_time": datetime.now()}
    user.orders.append(models.UserOrder(**date_time))
    db.commit()
    user_order = db.query(models.UserOrder).filter(models.UserOrder.user_id == user.id and 
                                           models.UserOrder.date_time == date_time["date_time"]
                                   ).order_by(models.UserOrder.id.desc()).first()
    return user_order


def create_products_order(db: Session, order: schemas.UserOrder, 
                         products_order_in: list[schemas.Order_In]
                         ):
    for prod in products_order_in:
        order.products.append(models.Product_Order(**prod.dict()))
        db.commit()
    return products_order_in


    





