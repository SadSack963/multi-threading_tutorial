# Python Threading Tutorial: Run Code Concurrently Using the Threading Module
# Corey Schafer
# https://www.youtube.com/watch?v=IEEhzQoKtQU

import time
import threading
import concurrent.futures


# IO Bound tasks benefit from multi-threading
# CPU Bound tasks benefit from multi-processing


def do_something(seconds=1):
    print(f'Sleeping {seconds} seconds...')
    time.sleep(seconds)
    print('Done sleeping.')


def old_method():
    # Old Method - manually creating threads
    # Create two threads
    thread_1 = threading.Thread(target=do_something)
    thread_2 = threading.Thread(target=do_something)

    # Start the threads
    thread_1.start()
    thread_2.start()
    # Wait for the threads to terminate
    thread_1.join()
    thread_2.join()


def loop():
    # Old Method - manually creating threads
    thread_list = []
    for _ in range(10):
        thread = threading.Thread(target=do_something, args=[1.5])
        thread.start()
        thread_list.append(thread)

    for thread in thread_list:
        thread.join()


def do_something_new(seconds=1):
    print(f'Sleeping {seconds} seconds...')
    time.sleep(seconds)
    return f'Done sleeping {seconds} seconds.'


def new_method():
    # ThreadPoolExecutor is an Executor subclass that uses a pool of threads to execute calls asynchronously
    # Best used with a context manager (with)
    with concurrent.futures.ThreadPoolExecutor() as tpe:
        # submit() returns a future object
        future_1 = tpe.submit(do_something_new, 1.5)
        future_2 = tpe.submit(do_something_new, 1.5)
        print(future_1.result())
        print(future_2.result())


def loop_new_method():
    second_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as tpe:
        # submit() returns a future object
        futures = [tpe.submit(do_something_new, second) for second in second_list]
        # Inside the with block, this prints each result as it completes
        for future in concurrent.futures.as_completed(futures):
            # NOTE that exceptions are raised when the result is returned!
            # So exceptions need to be handled here
            print(future.result())
    # # This prints results in a random order
    # for future in concurrent.futures.as_completed(futures):
    #     print(future.result())


def executor_map():
    second_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    with concurrent.futures.ThreadPoolExecutor() as tpe:
        futures = tpe.map(do_something_new, second_list)
        # map() returns the results in the order that they were started
        for future in futures:
            # NOTE that exceptions are raised when the result is returned!
            # So exceptions need to be handled here
            print(future)


if __name__ == '__main__':
    start = time.perf_counter()

    # Synchronous task
    # ================
    # do_something()

    # Multi-threading
    # ===============
    #   Note that although threads run concurrently,
    #   they do not start running at exactly the same time.
    # old_method()
    # loop()
    # new_method()
    # loop_new_method()
    executor_map()

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second.')
