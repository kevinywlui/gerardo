"""Example usage of decorators.
"""
import os
from gerardo import psql_insert, psql_mp_insert, psql_handler

# Get `PGHOST` environment variable
pghost = os.environ["PGHOST"]

# Insert into a table called `example_db`
DSN = {"host": pghost, "port": "", "user": "", "password": "", "dbname": "example_db"}

# Table will be called `test_table`
PSQL_TABLE = "test_table"

# There are two columns called `x` and `y`. They both contain `INT`.
COLUMNS = [("x", "INT"), ("y", "INT")]

# Set a psql handler
PH = psql_handler(DSN, PSQL_TABLE, COLUMNS)

# This transform `f` into a function that applies `f` to a list of arguments in
# parallel and inserts into a table. Currently, we only handle the
# single-variable case.
@psql_mp_insert(PH)
def f(x):
    return (x[0] + x[1], x[0] * x[1])


# Actually compute with `f`.
list_args = [(x, y) for x in range(5) for y in range(10)]
f(list_args)

# Alternatively we can do this in not-parallel.
@psql_insert(PH)
def g(x, y):
    return (x, x + y)


g(3, 4)
