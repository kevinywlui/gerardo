# gerardo

[![PyPI version](https://badge.fury.io/py/gerardo.svg)](https://badge.fury.io/py/gerardo)

**gerardo** provides decorators to easily compute in parallel and store the
results in a PostgreSQL database.

## Usage

See `examples/example.py` for more details.

```python
from gerardo import psql_mp_insert, psql_handler

# Set a PostgreSQL handler
pghost = os.environ["PGHOST"]
DSN = {
    "host": pghost,
    "port": "",
    "user": "",
    "password": "",
    "dbname": "example_db",
}
PSQL_TABLE = "test_table"
COLUMNS = [('x', 'INT'), ('y', 'INT')]

PH = psql_handler(DSN, PSQL_TABLE, COLUMNS)

# Define a single-variable function.
@psql_mp_insert(PH)
def f(x):
    return (x[0]+x[1], x[0]*x[1])

# Compute by forming a list of arguments
list_args = [(x, y) for x in range(5) for y in range(10)]
f(list_args)
```

## Installation

```
pip install gerardo --user
```


## Homepage

* https://github.com/kevinywlui/gerardo
