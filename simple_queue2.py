#!/usr/bin/python3

from multiprocessing import Queue, Process, current_process


def worker(queue):
    name = current_process().name
    print(f'{name} data received: {queue.get()}')


def main():

    queue = Queue()
    queue.put("wood")
    queue.put("sky")
    queue.put("cloud")
    queue.put("ocean")

    processes = [Process(target=worker, args=(queue,)) for _ in range(4)]

    for p in processes:
        p.start()

    for p in processes:
        p.join()


if __name__ == "__main__":
    main()
