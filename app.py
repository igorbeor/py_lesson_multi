from jobs import get_jobs_threading, get_jobs_multiprocessing
from factorial import factorial_threading, factorial_multiprocessing
from queue import Queue
import logging

logging.basicConfig(
    filename='app.log',
    filemode='w',
    level=logging.DEBUG
)

if __name__ == '__main__':
    job_result = Queue()
    get_jobs_threading(['python', 'php', 'ruby'], [1, 2], job_result)
    factorial_threading_result = Queue()
    factorial_threading([3, 5, 7], factorial_threading_result)
