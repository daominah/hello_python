import threading
from typing import List


class Data:
    def __init__(self):
        self.f1: List[int] = []
        self.lock = threading.Lock()


def worker(i: int, data: Data):
    for j in range(1000 * i, 1000 * (i + 1)):
        data.lock.acquire()
        local = data.f1[:]
        local.append(j)
        data.f1 = local
        data.lock.release()


threads: List[threading.Thread] = []
data = Data()
for i in range(20):
    t = threading.Thread(target=worker, args=(i, data))
    threads.append(t)
    t.start()
for i in range(20):
    threads[i].join()

print(len(data.f1), data.f1)
