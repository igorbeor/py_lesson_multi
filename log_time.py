from time import time
from functools import wraps
import logging


def log_time(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        start = time()
        result = fn(*args, **kwargs)
        end = time()
        logging.debug(f'Function {fn.__name__.upper()}. Time spent: {end - start}')
        return result
    return wrapper