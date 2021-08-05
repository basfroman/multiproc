#!/usr/bin/python3

from multiprocessing import Process, Queue, current_process
import random


def rand_val(queue):

    num = random.random()
    queue.put({current_process().name: num})


def main():

    queue = Queue()

    processes = [Process(target=rand_val, args=(queue,)) for _ in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()

    results = [queue.get() for _ in processes]
    print(results)


if __name__ == "__main__":
    main()
