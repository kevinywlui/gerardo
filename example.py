import multiprocessing
import os
from gerardo import psql_insert, psql_handler

pghost = os.environ["PGHOST"]
DSN = {
    "host": pghost,
    "port": "",
    "user": "",
    "password": "",
    "dbname": "test_temp",
}
PSQL_TABLE = "test_table"
COLUMNS = [('x', 'INT'), ('x2', 'INT')]

PH = psql_handler(DSN, PSQL_TABLE, COLUMNS)

@psql_insert(PH)
def f(x):
    return x, x**2

with multiprocessing.Pool() as p:
    p.map(f, range(10**6))
