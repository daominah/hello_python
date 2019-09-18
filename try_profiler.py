import multiprocessing
import cProfile
import time
import typing
import math


def f1(num):
    s = 1
    for i in range(1000000):
        s = s + i
    print("f1", num, s)


def f2(num):
    s = 1
    for i in range(1000000):
        s = s + math.log(100 + i)
    print("f2", num, s)


if __name__ == '__main__':
    for i in range(5):
        target: typing.Callable[[float], None] = None
        if i % 2:
            target = f1
        else:
            target = f2
        target(i)
