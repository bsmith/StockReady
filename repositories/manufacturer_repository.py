from db.run_sql import run_sql
from models.manufacturer import Manufacturer

SQL_SELECT = """SELECT full_name, short_brand_name, trade_website, trade_telephone, customer_website, customer_telephone, id FROM manufacturers WHERE id = %s"""
SQL_SELECT_ALL = """SELECT full_name, short_brand_name, trade_website, trade_telephone, customer_website, customer_telephone, id FROM manufacturers"""

def _make_model_from_select_row(row):
    columns = 'full_name', 'short_brand_name', 'trade_website', 'trade_telephone', 'customer_website', 'customer_telephone', 'id'
    manufacturer = Manufacturer(*[row[column] for column in columns])
    return manufacturer

def select(id):
    results = run_sql(SQL_SELECT, [id])
    if results:
        return _make_model_from_select_row(results[0])
    return None

def select_all():
    results = run_sql(SQL_SELECT_ALL)
    manufacturers = [_make_model_from_select_row(row) for row in results]
    return manufacturers

SQL_DELETE = """DELETE FROM manufacturers WHERE id = %s"""
SQL_DELETE_ALL = """DELETE FROM manufacturers"""

# XXX No error handling for id not found
def delete(id):
    run_sql(SQL_DELETE, [id], do_fetchall=False)

def delete_all():
    run_sql(SQL_DELETE_ALL, do_fetchall=False)

SQL_INSERT = """INSERT INTO manufacturers (full_name, short_brand_name, trade_website, trade_telephone, customer_website, customer_telephone) VALUES (""" + ", ".join(["%s"]*6) + """) RETURNING id"""
SQL_UPDATE = """UPDATE manufacturers SET (full_name, short_brand_name, trade_website, trade_telephone, customer_website, customer_telephone) = (""" + ", ".join(["%s"]*6) + """) WHERE id = %s"""

def _make_insert_row_from_model(manufacturer):
    attrs = 'full_name', 'short_brand_name', 'trade_website', 'trade_telephone', 'customer_website', 'customer_telephone'
    return [getattr(manufacturer, attr) for attr in attrs]

# XXX No error handling for couldn't save
def save(manufacturer):
    values = _make_insert_row_from_model(manufacturer)
    results = run_sql(SQL_INSERT, values)
    manufacturer.id = results[0]['id']
    return manufacturer

# XXX No error handling for couldn't update
def update(manufacturer):
    values = _make_insert_row_from_model(manufacturer)
    values += [manufacturer.id]
    run_sql(SQL_UPDATE, values, do_fetchall=False)
    return manufacturer

SQL_COUNT_PRODUCTS = "SELECT COUNT(id) AS count FROM products WHERE manufacturer_id = %s"

def count_products_from_manufacturer(id):
    results = run_sql(SQL_COUNT_PRODUCTS, [id])
    return results[0]['count']