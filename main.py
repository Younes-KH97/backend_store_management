from fastapi import FastAPI

from routers import categories, product_types, products, roles, users

from sqlalchemy import event
from database import engine
import models

models.Base.metadata.create_all(bind=engine)

@event.listens_for(engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

app = FastAPI()


app.include_router(categories.router)
app.include_router(products.router)
app.include_router(product_types.router)
app.include_router(users.router)
app.include_router(roles.router)

