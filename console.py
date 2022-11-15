"""console.py

Run this with `python -i console.py` to load a set of application modules,
and be placed in a REPL.

Alternatively, enable pdb, add code to this file, and place `pdb.set_trace()`
where you'd like to start debugging.
"""

# import pdb
import logging
from decimal import Decimal

from db.run_sql import run_sql
from models.product_type import ProductType
from models.manufacturer import Manufacturer
from models.product import Product
import repositories.product_type_repository as product_type_repository
import repositories.manufacturer_repository as manufacturer_repository
import repositories.product_repository as product_repository

logging.basicConfig(level=logging.DEBUG)

# EXAMPLE: show all data in database
# print(run_sql("SELECT * FROM product_types;"))
# print(run_sql("SELECT * FROM manufacturers;"))
# print(run_sql("SELECT * FROM products"))

# Exercise the Product Type Repository
if False:
    print("Exercising Product Type Repository")
    all_types = product_type_repository.select_all()
    for type in all_types:
        print("select_all:", type)
    one_type = product_type_repository.select(all_types[0].id)
    print("select:", one_type)
    new_type = ProductType("New Type")
    product_type_repository.save(new_type)
    print("save:", new_type)
    new_type.name = "Old Type"
    product_type_repository.update(new_type)
    print("update:", product_type_repository.select(new_type.id))
    product_type_repository.delete(new_type.id)
    print("")

# Exercise the Manufacturer Repository
if False:
    print("Exercising Manufacturer Repository")
    all_manufacturers = manufacturer_repository.select_all()
    for manufacturer in all_manufacturers:
        print("select_all:", manufacturer.__dict__)
    one_manufacturer = manufacturer_repository.select(all_manufacturers[0].id)
    print("select:", one_manufacturer.__dict__)
    new_manufacturer = Manufacturer("New Manufacturer", "NEW")
    manufacturer_repository.save(new_manufacturer)
    print("save:", new_manufacturer.__dict__)
    new_manufacturer.customer_website = "https://new.com"
    manufacturer_repository.update(new_manufacturer)
    print("update:", manufacturer_repository.select(new_manufacturer.id).__dict__)
    manufacturer_repository.delete(new_manufacturer.id)
    print("")

# Exercise the Product Repository
if True:
    all_products = product_repository.select_all()
    for product in all_products:
        print("select_all:", product.__dict__)
    one_product = product_repository.select(all_products[0].id)
    print("select:", one_product.__dict__)
    manufacturer = manufacturer_repository.select_all()[-1]
    product_type = product_type_repository.select_all()[-1]
    new_product = Product("MPN", manufacturer, "Short", None, product_type,
        None, 0, Decimal(10), Decimal(20), discontinued=False)
    product_repository.save(new_product)
    print("save:", new_product.__dict__)
    new_product.screen_size = 20
    new_product.discontinued = True
    product_repository.update(new_product)
    print("update:", product_repository.select(new_product.id).__dict__)
    product_repository.delete(new_product.id)
    print("")

# pdb.set_trace()
