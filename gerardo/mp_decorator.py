from multiprocessing import Pool


def parallel(func):
    def wrapper(*args, **kwargs):
        with Pool() as pool:
            print(pool.map(func, [1, 2, 3]))
    return wrapper

@parallel
def f(x):
    return x*x

f(2)
