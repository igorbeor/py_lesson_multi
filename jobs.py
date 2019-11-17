from threading import Thread
from multiprocessing import Pool
import requests
from log_time import log_time
from queue import Queue


BASE_URL = 'https://jobs.github.com/positions.json'

def get_job_info(option: str, page: int, queue: Queue = None):
    response = requests.get(BASE_URL, params={'option': option, 'page': page})
    if not queue:
        return response.content
    queue.put(response.content)

@log_time
def get_jobs_threading(options: list, pages: list, queue: Queue):
    threads = list()
    for option in options:
        for page in pages:
            threads.append(Thread(target=get_job_info, args=(option, page, queue,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()

@log_time
def get_jobs_multiprocessing(options: list, pages: list):
    result = list()
    processes = len(options) * len(pages)
    pool = Pool(processes=processes)
    for option in options:
        for page in pages:
            result.append(pool.apply_async(get_job_info, [option, page]).get())
    pool.close()
    pool.join()
    return result

