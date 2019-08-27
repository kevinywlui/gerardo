import multiprocessing
import os
import functools
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



def mp(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        with multiprocessing.Pool() as p:
            return p.map(f, args)
    return wrapper


@psql_insert(PH)
def f(x):
    return x, x**2
