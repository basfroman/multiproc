#!/usr/bin/python3

from multiprocessing import Process, Value, cpu_count, current_process
from random import random
from time import sleep


def f(counter):

    sleep(1)

    with counter.get_lock():
        counter.value += 1
    print(f'Counter in {current_process().name}:\t{counter.value}')


def main():
    # type code - https://docs.python.org/3/library/array.html#module-array
    counter = Value('i', 10)

    processes = [Process(target=f, args=(counter, )) for _ in range(cpu_count()*2)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


if __name__ == '__main__':
    main()
