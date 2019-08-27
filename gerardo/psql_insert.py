"""Module that defines the psycopg2_decorator.
"""
import psycopg2
import functools

class psql_handler:
    def __init__(self, dsn, table, columns):
        self.table = table
        self.dsn = dsn
        with psycopg2.connect(**dsn) as conn:
            with conn.cursor() as c:
                c.execute(f"DROP TABLE if exists {table};")

                # form table with columns
                start = f"CREATE TABLE {table} ("
                mid = ''.join([f"{x[0]} {x[1]}," for x in columns])[:-1]
                end = ");"
                full = start + mid + end
                c.execute(full)

    def insert(self, result):
        with psycopg2.connect(**self.dsn) as conn:
            with conn.cursor() as c:
                start = f"INSERT INTO {self.table} VALUES ("
                mid = ''.join([f"{x} ," for x in result])[:-1]
                end = ");"
                full = start + mid + end
                c.execute(full)


def psql_insert(PH):
    def psql_inner(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            PH.insert(result)
            return result
        return wrapper
    return psql_inner
