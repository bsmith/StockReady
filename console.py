"""console.py

Run this with `python -i console.py` to load a set of application modules,
and be placed in a REPL.

Alternatively, enable pdb, add code to this file, and place `pdb.set_trace()`
where you'd like to start debugging.
"""

# import pdb
import logging

from db.run_sql import run_sql
from models.product_type import ProductType
import repositories.product_type_repository as product_type_repository

logging.basicConfig(level=logging.DEBUG)

# EXAMPLE: show all data in database
# print(run_sql("SELECT * FROM product_types;"))
# print(run_sql("SELECT * FROM manufacturers;"))
# print(run_sql("SELECT * FROM products"))

# Exercise the Product Type Repository
print("Exercising Product Type Repository")
all_types = product_type_repository.select_all()
for type in all_types:
    print("select_all", type)
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

# pdb.set_trace()
