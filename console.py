"""console.py

Run this with `python -i console.py` to load a set of application modules,
and be placed in a REPL.

Alternatively, enable pdb, add code to this file, and place `pdb.set_trace()`
where you'd like to start debugging.
"""

# import pdb

from db.run_sql import run_sql

# EXAMPLE: show all data in database
print(run_sql("SELECT * FROM product_types;"))
print(run_sql("SELECT * FROM manufacturers;"))
print(run_sql("SELECT * FROM products"))

# pdb.set_trace()
