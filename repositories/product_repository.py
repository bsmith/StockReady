from db.run_sql import run_sql
from models.product import Product
import repositories.product_type_repository as product_type_repository
import repositories.manufacturer_repository as manufacturer_repository

SQL_SELECT_FIELDS="mpn, manufacturer_id, short_description, long_description, product_type_id, screen_size, stock_on_hand, cost_price, retail_price, discontinued, id"
SQL_SELECT = "SELECT " + SQL_SELECT_FIELDS + " FROM products WHERE id = %s"
SQL_SELECT_ALL = "SELECT " + SQL_SELECT_FIELDS + " FROM products ORDER BY manufacturer_id ASC, id ASC"""
SQL_SELECT_DC = "SELECT " + SQL_SELECT_FIELDS + " FROM products WHERE discontinued = TRUE"

class _ModelMakerWithCache:
    def __init__(self):
        self.manufacturer_cache = {}
        self.product_type_cache = {}

    def get_product_type_by_id(self, id):
        if id in self.product_type_cache:
            return self.product_type_cache[id]
        product_type = product_type_repository.select(id)
        self.product_type_cache[id] = product_type
        return product_type
    
    def get_manufacturer_by_id(self, id):
        if id in self.manufacturer_cache:
            return self.manufacturer_cache[id]
        manufacturer = manufacturer_repository.select(id)
        self.manufacturer_cache[id] = manufacturer
        return manufacturer

    def make_model_from_select_row(self, row):
        columns = 'mpn', 'short_description', 'long_description', 'screen_size', 'stock_on_hand', 'cost_price', 'retail_price', 'discontinued', 'id'
        kwargs = dict((column, row[column]) for column in columns)
        manufacturer = self.get_manufacturer_by_id(row['manufacturer_id'])
        product_type = self.get_product_type_by_id(row['product_type_id'])
        product = Product(manufacturer=manufacturer, product_type=product_type, **kwargs)
        return product

def select(id):
    results = run_sql(SQL_SELECT, [id])
    if results:
        model_maker = _ModelMakerWithCache()
        return model_maker.make_model_from_select_row(results[0])
    return None

def select_all():
    results = run_sql(SQL_SELECT_ALL)
    model_maker = _ModelMakerWithCache()
    products = [model_maker.make_model_from_select_row(row) for row in results]
    return products

def select_discontinued():
    results = run_sql(SQL_SELECT_DC)
    model_maker = _ModelMakerWithCache()
    products = [model_maker.make_model_from_select_row(row) for row in results]
    return products

SQL_DELETE = """DELETE FROM products WHERE id = %s"""
SQL_DELETE_ALL = """DELETE FROM products"""

# XXX No error handling for id not found
def delete(id):
    run_sql(SQL_DELETE, [id], do_fetchall=False)

def delete_all():
    run_sql(SQL_DELETE_ALL, do_fetchall=False)

##### NOT UPDATED BELOW HERE

SQL_INSERT = """INSERT INTO products (mpn, manufacturer_id, short_description, long_description, product_type_id, screen_size, stock_on_hand, cost_price, retail_price, discontinued) VALUES (""" + ", ".join(["%s"]*10) + """) RETURNING id"""
SQL_UPDATE = """UPDATE products SET (mpn, manufacturer_id, short_description, long_description, product_type_id, screen_size, stock_on_hand, cost_price, retail_price, discontinued) = (""" + ", ".join(["%s"]*10) + """) WHERE id = %s"""

def _make_insert_row_from_model(product):
    attrs = 'mpn', 'manufacturer', 'short_description', 'long_description', 'product_type', 'screen_size', 'stock_on_hand', 'cost_price', 'retail_price', 'discontinued'
    row = [getattr(product, attr) for attr in attrs]
    row[attrs.index('manufacturer')] = product.manufacturer.id
    row[attrs.index('product_type')] = product.product_type.id
    return row

# XXX No error handling for couldn't save
def save(product):
    values = _make_insert_row_from_model(product)
    results = run_sql(SQL_INSERT, values)
    product.id = results[0]['id']
    return product

# XXX No error handling for couldn't update
def update(product):
    values = _make_insert_row_from_model(product)
    values += [product.id]
    run_sql(SQL_UPDATE, values, do_fetchall=False)
    return product