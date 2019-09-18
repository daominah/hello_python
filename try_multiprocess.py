from multiprocessing import Pipe, Process, Queue
from multiprocessing.connection import Connection
from typing import List
import time, datetime, os


def worker_start(q: Queue):
    nloop = 0
    child_pid = os.getpid()
    while True:
        nloop += 1
        # print("child {}: loop {}".format(child_pid, nloop))
        try:
            time.sleep(2)
            msg = q.get(block=True, timeout=1)
            print("child {} msg: {}".format(child_pid, msg))
        except:
            # empty queue
            pass


children: List[Process] = []
g_queue = Queue()

for i in range(0, 3):
    child = Process(target=worker_start, args=(g_queue,))
    children.append(child)
for child in children:
    child.start()

print("parent pid", os.getpid())
i = 0
while True:
    i += 1
    print("parent loop {}".format(i))
    g_queue.put(datetime.datetime.now())
    print("qsize", g_queue.qsize())
    time.sleep(0.5)
