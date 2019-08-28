"""Example usage of decorators.
"""
import multiprocessing
import os
from gerardo import psql_insert, psql_mp_insert, psql_handler

# Get `PGHOST` environment variable
pghost = os.environ["PGHOST"]

# Insert into a table called `example_db`
DSN = {
    "host": pghost,
    "port": "",
    "user": "",
    "password": "",
    "dbname": "example_db",
}

# Table will be called `test_table`
PSQL_TABLE = "test_table"

# There are two columns called `x` and `y`. They both contain `INT`.
COLUMNS = [('x', 'INT'), ('y', 'INT')]

# Set a psql handler
PH = psql_handler(DSN, PSQL_TABLE, COLUMNS)

# This transform `f` into a function that applies `f` to a list of arguments in
# parallel and inserts into a table
@psql_mp_insert(PH)
def f(x, y):
    return (x+y, x*y)

# Actually compute with `f`.
l = [(x,y) for x in range(5) for y in range(10)]
f(*l)
