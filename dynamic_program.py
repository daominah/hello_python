from typing import Dict

def f(n):
    if n <= 2:
        return 1
    else:
        return f(n - 1) + f(n - 2)


cache: Dict[int, int] = {}


def f2(n):
    global cache
    if n in cache:
        return cache[n]
    if n <= 2:
        cache[n] = 1
        return 1
    else:
        r = f2(n-1) + f2(n-2)
        cache[n] = r
        return r


print(f2(500))
