import time
from math import sqrt

def logging_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('Start time: {};\nEnd time: {};\nOverall: {}.'.format(start, end, end - start))
    return wrapper

@logging_decorator
def double_sqrt(x):
    return sqrt(sqrt(x))

double_sqrt(18105056156100160610)
