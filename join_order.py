#!/usr/bin/python3
"""
It shows that .join() waits while child process to be terminated and then continues execution code.
"""

from multiprocessing import Process
import time


def fun(val):

    print(f'starting fun with {val} s')
    time.sleep(val)
    print(f'finishing fun with {val} s')


def main(join=False):

    p1 = Process(target=fun, args=(3, ))
    p1.start()
    if join:
        p1.join()

    p2 = Process(target=fun, args=(2, ))
    p2.start()
    if join:
        p2.join()

    p3 = Process(target=fun, args=(1, ))
    p3.start()
    if join:
        p3.join()

    if not join:
        p1.join()
        p2.join()
        p3.join()

    print('finished main')


if __name__ == '__main__':
    # True/False as join argument
    main(join=True)
