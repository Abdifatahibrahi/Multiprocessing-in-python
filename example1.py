import multiprocessing
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor
import time


start = time.perf_counter()

def do_something(seconds):
    print(f'sleeping {seconds} second')
    time.sleep(seconds)
    return f'Done sleeping..{seconds} seconds'

processes = []

if __name__ == '__main__':

    # with ProcessPoolExecutor() as executor:
    #    secs = [5,4,3,2,1]
    #    results = [executor.submit(do_something, sec) for sec in secs]
    #    for f in concurrent.futures.as_completed(results):
    #     print(f.result())

    with ProcessPoolExecutor() as executor:
       secs = [5,4,3,2,1]
       results = executor.map(do_something, secs)

       for result in results:
        print(result)

        


    # for _ in range(20):
    #     p = multiprocessing.Process(target=do_something, args=[1])
    #     p.start()
    #     processes.append(p)

    # for process in processes:
    #     process.join()



    finish = time.perf_counter()

    print(f'Finished in {round(finish-start, 2)} seconds')