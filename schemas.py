from datetime import datetime
from typing import List, Union
from pydantic import BaseModel, Field


class ProductTypeBase(BaseModel):
    name: Union[str, None] = None

class ProductType(ProductTypeBase):
    id: int
    class Config:
        orm_mode = True

class ProductBase(BaseModel):
    title: str
    description: Union[str, None] = None
    price: float
    time: float
    photo_url: str
    

class Product(ProductBase):
    id: int
    category_id: int
    product_types: list[ProductType] = []

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    name: str
    photo_url: str

class Category(CategoryBase):
    id: int
    products: list[Product] = []

    class Config:
        orm_mode = True


##
#
#

###
class Product_Order_In(BaseModel):
    product_id: int
    quantity: int

class Order_In(BaseModel):
    products: list[Product_Order_In]
    
class Product_Order(BaseModel):
    product_id: int
    order_id: int
    quantity: int
    
    class Config:
        orm_mode = True

class UserOrder(BaseModel):
    id: int
    date_time: datetime
    user_id: int
    products: list[Product_Order] = []

    class Config:
        orm_mode = True



###


class RoleBase(BaseModel):
    name: str

class Role(RoleBase):
    id: int

    class Config:
        orm_mode = True

class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str



class User(UserCreate):
    id: int
    roles: list[Role] = []
    wish_list: list[Product] = []
    orders: list[UserOrder] = []

    class Config:
        orm_mode = True






    # __tablename__ = "user"

    # id = Column(Integer, primary_key=True, index=True)
    # username = Column(String(80), index = True)
    # email = Column(String(120))
    # password = Column(String(80))

    # roles = relationship(
    #     "Role", secondary=user_role, back_populates="users", cascade="all, delete"
    # )