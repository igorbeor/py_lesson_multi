from threading import Thread
from multiprocessing import Pool
from time import time
from queue import Queue
from log_time import log_time
from functools import reduce
from operator import mul

def factorial(number: int, queue: Queue = None):
    if number == 0 or number == 1:
        result = 1
    result = reduce(mul, list(range(2, number + 1)))
    if queue:
        queue.put(result)
        return
    return result
    

@log_time
def factorial_threading(numbers: list, queue: Queue):
    threads = list()
    for number in numbers:
        threads.append(Thread(target=factorial, args=(number, queue,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

@log_time
def factorial_multiprocessing(numbers: list):
    result = list()
    pool = Pool(processes=3)
    for number in numbers:
        result.append(pool.apply_async(factorial, [number]).get())
    pool.close()
    pool.join()
    return result





# if __name__ == '__main__':
    # t1 = Thread(target=factorial, args=(3,))
    # t2 = Thread(target=factorial, args=(5,))
    # t3 = Thread(target=factorial, args=(7,))

    # start = time()
    # t1.start()
    # t2.start()
    # t3.start()
    # t1.join()
    # t2.join()
    # t3.join()
    # end = time()
    # print(f'THREADING! Time spent: {end - start}')

    # start = time()
    # pool = Pool(processes=3)
    # r1 = pool.apply_async(factorial, [3])
    # r2 = pool.apply_async(factorial, [5])
    # r3 = pool.apply_async(factorial, [7])
    # pool.close()
    # pool.join()
    # end = time()
    # print(f'PROCESSING! Time spent: {end - start}')

    print(factorial(5))
