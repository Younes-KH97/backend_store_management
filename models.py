from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Table, Text
from sqlalchemy.orm import relationship

from database import Base


class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), index = True)
    photo_url = Column(String(220))

    products = relationship("Product", back_populates="category", cascade="all, delete",
        passive_deletes=True)


user_wish = Table(
    "user_wish",
    Base.metadata,
    Column("user_id", ForeignKey("user.id", ondelete = "CASCADE"), primary_key=True),
    Column("product_id", ForeignKey("product.id", ondelete = "CASCADE"), primary_key=True)
)

class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(80), index=True)
    description = Column(String(180), index=True)
    price = Column(Float)
    time = Column(Float)
    photo_url = Column(String(220))
    category_id = Column(Integer, ForeignKey("category.id", ondelete="CASCADE"))
    category = relationship("Category", back_populates="products")

    product_types = relationship("ProductType", back_populates="product", cascade="all, delete",
        passive_deletes=True)

    wish_users = relationship(
        "User", secondary = user_wish, back_populates="wish_list"
    )

    orders = relationship("Product_Order", back_populates="product", cascade = "all, delete",
        passive_deletes = True)



class ProductType(Base):
    __tablename__ = "product_type"

    id = Column(Integer, primary_key=True)
    name = Column(String(80))

    product_id = Column(Integer, ForeignKey("product.id", ondelete="CASCADE"))
    product = relationship("Product", back_populates="product_types")

user_role = Table(
    "user_role",
    Base.metadata,
    Column("user_id", ForeignKey("user.id", ondelete = "CASCADE"), primary_key=True),
    Column("role_id", ForeignKey("role.id", ondelete = "CASCADE"), primary_key=True)
)

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(80), index = True)
    email = Column(String(120))
    password = Column(String(80))

    roles = relationship(
        "Role", secondary=user_role, back_populates="users"
    )

    wish_list = relationship(
        "Product", secondary=user_wish, back_populates="wish_users"
    )

    orders = relationship(
        "UserOrder", back_populates="owner", cascade="all, delete",
        passive_deletes=True
    )


class Role(Base):
    __tablename__ = "role"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(80), index = True)

    users = relationship(
        "User", secondary=user_role, back_populates="roles"
    )




class UserOrder(Base):
    __tablename__ = "user_order"

    id = Column(Integer, primary_key = True, index = True)
    date_time = Column(DateTime)

    user_id = Column(Integer, ForeignKey("user.id", ondelete="CASCADE"))
    owner = relationship("User", back_populates="orders")

    # This products is of type: Product_Order
    products = relationship("Product_Order", back_populates="order", cascade = 'all, delete',
                            passive_deletes = True)
    



class Product_Order(Base):
    __tablename__ = "product_order"
    product_id = Column(ForeignKey("product.id", ondelete = 'cascade'), primary_key=True)
    order_id = Column(ForeignKey("user_order.id", ondelete = 'cascade'), primary_key=True)
    quantity = Column(Integer)
    
    product = relationship("Product", back_populates="orders")
    order = relationship("UserOrder", back_populates="products")



    
    