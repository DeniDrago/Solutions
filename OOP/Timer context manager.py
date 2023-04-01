from contextlib import contextmanager
from time import time


@contextmanager
def timer():
    start_time = time()
    try:
        yield
    except Exception as e:
        print(f'Error: {type(e).__name__} - {e}')
    else:
        end_time = time()
        print(f"Operation executed in {end_time - start_time:.6f} seconds")


class Timer:

    def __init__(self):
        pass

    def __enter__(self):
        self.start_time = time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print(f'Error: {exc_type.__name__} - {exc_val}')
        else:
            self.end_time = time()
            print(f"Operation executed in {self.end_time - self.start_time:.6f} seconds")


if __name__ == '__main__':
    with timer() as t:
        result = [2 ** 1000 for i in range(100000)]

    with Timer() as t1:
        result1 = [2 ** 1000 for i in range(100000)]
