#!/usr/bin/python

from multiprocessing import Pool
import functools


def one(x):
    return x + 1


def two(x):
    return x - 1


def three(x, y):
    return x + y


def func_call(f):
    return f()


def main():
    f_one = functools.partial(one, 4)
    f_two = functools.partial(two, 2)
    f_three = functools.partial(three, 3, 4)

    with Pool() as pool:
        res = pool.map(func_call, [f_one, f_two, f_three])
        print(res)


if __name__ == '__main__':
    main()
