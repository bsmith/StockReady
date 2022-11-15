from db.run_sql import run_sql
from models.product_type import ProductType

SQL_SELECT = """SELECT name, id FROM product_types WHERE id = %s"""
SQL_SELECT_ALL = """SELECT name, id FROM product_types ORDER BY name ASC"""

def _make_model_from_select_row(row):
    product_type = ProductType(row['name'], row['id'])
    return product_type

def select(id):
    results = run_sql(SQL_SELECT, [id])
    if results:
        return _make_model_from_select_row(results[0])
    return None

def select_all():
    results = run_sql(SQL_SELECT_ALL)
    product_types = [_make_model_from_select_row(row) for row in results]
    return product_types

SQL_DELETE = """DELETE FROM product_types WHERE id = %s"""
SQL_DELETE_ALL = """DELETE FROM product_types"""

# XXX No error handling for id not found
def delete(id):
    run_sql(SQL_DELETE, [id], do_fetchall=False)

def delete_all():
    run_sql(SQL_DELETE_ALL, do_fetchall=False)

SQL_INSERT = """INSERT INTO product_types (name) VALUES (%s) RETURNING id"""
SQL_UPDATE = """UPDATE product_types SET name = %s WHERE id = %s"""

def _make_insert_row_from_model(product_type):
    return [product_type.name]

# XXX No error handling for couldn't save
def save(product_type):
    values = _make_insert_row_from_model(product_type)
    results = run_sql(SQL_INSERT, values)
    product_type.id = results[0]['id']
    return product_type

# XXX No error handling for couldn't update
def update(product_type):
    values = _make_insert_row_from_model(product_type)
    values += [product_type.id]
    run_sql(SQL_UPDATE, values, do_fetchall=False)
    return product_type