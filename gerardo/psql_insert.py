"""Module that defines the psycopg2_decorator.
"""
import psycopg2

class psql_insert:
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

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            self.insert(result)
            return result
        return wrapper

    def insert(self, result):
        with psycopg2.connect(**self.dsn) as conn:
            with conn.cursor() as c:
                start = f"INSERT INTO {self.table} VALUES ("
                mid = ''.join([f"{x} ," for x in result])[:-1]
                end = ");"
                full = start + mid + end
                c.execute(full)
