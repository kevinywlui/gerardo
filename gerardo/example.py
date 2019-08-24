import os
from gerardo import psql_insert

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

@psql_insert(DSN, PSQL_TABLE, COLUMNS)
def f(x):
    return (x, x**2)

[f(x) for x in range(100)]
