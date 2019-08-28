"""Module that defines decorators for working with PostgreSQL.

There are two decorators `psql_insert` and `psql_mp_insert`. The first inserts
the result of a function onto a PostgreSQL database. The second is the
multiprocessing version of the first but only for single variable functions.
"""

import functools

import psycopg2
from pathos.multiprocessing import ProcessPool


class psql_handler:
    """Handles interacting with PostgreSQL database.

    This class will initialize a connection and provide a method to insert a
    row.

    Args:
        dsn (dict): dictionary of the connection parameter.
        table (str): name of table.
        columns (List[Tuple[str, str]]): list of tuples where the first entry
            is the column name and the second entry is the type.
    """

    def __init__(self, dsn, table, columns):
        self.table = table
        self.dsn = dsn
        with psycopg2.connect(**dsn) as conn:
            with conn.cursor() as c:
                c.execute(f"DROP TABLE if exists {table};")

                # form table with columns
                start = f"CREATE TABLE {table} ("
                mid = "".join([f"{x[0]} {x[1]}," for x in columns])[:-1]
                end = ");"
                full = start + mid + end
                c.execute(full)

    def insert(self, row):
        """Insert a row into this psql table.

        Args:
            row (List[any]): a row of data to be inserted.
        """
        with psycopg2.connect(**self.dsn) as conn:
            with conn.cursor() as c:
                start = f"INSERT INTO {self.table} VALUES ("
                mid = "".join([f"{x} ," for x in row])[:-1]
                end = ");"
                full = start + mid + end
                c.execute(full)


def psql_insert(PH):
    """Decorator that insert the output of a function into a PostgreSQL
    database.

    Args:
        PH (psql_handler): the handler for the PostgreSQL database.

    Returns:
        function
    """

    def psql_inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            PH.insert(result)
            return result

        return wrapper

    return psql_inner


def psql_mp_insert(PH):
    """Decorator that insert the output of a function into a PostgreSQL
    database in parallel.

    The current draw back to this we only decorate single-variable functions.

    Args:
        PH (psql_handler): the handler for the PostgreSQL database.

    Returns:
        function
    """

    def psql_inner(func):
        def insert_func(*args):
            result = func(*args)
            PH.insert(result)
            return result

        @functools.wraps(func)
        def wrapper(*args):
            with ProcessPool() as p:
                p.map(insert_func, *args)

        return wrapper

    return psql_inner
