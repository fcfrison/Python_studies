import multiprocessing


def sq_data(data):
    print(data)
    return data**2


def print_process_name():
    print(f"process name = {multiprocessing.current_process().name}")


def main():
    pool_size = multiprocessing.cpu_count() * 2  # the number of cores multiplied by 2.
    pool = multiprocessing.Pool(
        processes=pool_size, initializer=print_process_name
    )  # instantiating a pool.
    print("right after pool creation")
    inputs = list(range(100))
    outputs = pool.map(func=sq_data, iterable=inputs)  # mapping the iterable data.
    print(outputs)
    print(f"len(outputs) = {len(outputs)}")
    pool.close()  # closing the process object. Releasing resources used.
    pool.join()


if __name__ == "__main__":
    main()
