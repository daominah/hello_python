import math

d = {}


def f(n):
    if n in d:
        return d[n]
    if n <= 2:
        r = 1
        d[n] = r
        return r
    else:
        r = f(n - 1) + f(n - 2) + 1
        d[n] = r
        return r


def s(n):
    return n * (n + 1) / 2 * 2 / 2


print(f(10))

if f(10) != 55: print("sai roi")
if f(9) != 34: print("sai roi")
if f(2) != 1: print("sai roi")
