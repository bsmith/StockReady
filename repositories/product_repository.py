from db.run_sql import run_sql
from models.manufacturer import Manufacturer
from models.product import Product
from models.product_type import ProductType

def select(id):
    raise NotImplementedError()

def select_all():
    raise NotImplementedError()

def delete(id):
    raise NotImplementedError()

def delete_all():
    raise NotImplementedError()

def save(product):
    raise NotImplementedError()

def update(product):
    raise NotImplementedError()